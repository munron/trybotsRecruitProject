# -*- coding: utf-8 -*-
# [名前] receiver.py
# [起動] python receiver.py "接続先グローバルip"
# [仕様] UDP hole punchingによるコネクション確立後、データを受信しサーボを動かす
# [備考]
#地上側でHTTP鯖を事前に起動させる
#streaming.pyより後のタイミングで起動させる必要がある

import pprint
import requests
import socket
import sys
import json
import os
import time
import RPi.GPIO as GPIO
import signal

param=sys.argv
remoteHost=param[1]
localHost='0.0.0.0'
port=25000
localAddr=(localHost,port)
remoteAddr=(remoteHost,port)
preSwimMode=0;

#Ctr-Cイベントハンドラ
def exit_handler(signal, frame):
    sys.error.write("\nExit")
    servoHeadYaw.stop()
    servoHeadPitch.stop()
    servoFoot.stop()
    GPIO.cleanup()
    sys.exit(0)
                            
signal.signal(signal.SIGINT, exit_handler)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
servoHeadRoll = GPIO.PWM(17, 50)
servoHeadPitch = GPIO.PWM(22, 50)
servoFoot = GPIO.PWM(24, 50)
servoHeadRoll.start(0.0)
servoHeadPitch.start(0.0)
servoFoot.start(0.0)

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(localAddr)
sys.stderr.write( "[receiver.py] : binded UDP socket to %s:%d\n" % localAddr)

#UDP hole punchingの処理
#本来ならばこのパケットは接続先のルーターに阻まれるはずであるが
#streaming.pyによってルーターが記録した経路でパケットが届く
sock.sendto("Hi!! this is receiver",remoteAddr)
sys.stderr.write("[receiver.py] : sended packet to %s:%d\n" % remoteAddr)
sf=sock.makefile()

def getServoPitch(pitch):
    if pitch > 0 and pitch < 45:
        servoHeadPitch.ChangeDutyCycle(7.0+2.0/45*pitch)
    elif pitch < 0 and pitch > -45:
        servoHeadPitch.ChangeDutyCycle(7.0+2.0/45*pitch)
    elif pitch > 45 :
        servoHeadPitch.ChangeDutyCycle(7.0+2.0)
    elif pitch < -45 :
        servoHeadPitch.ChangeDutyCycle(7.0-2.0)
    


def getServoRoll(roll):
    if roll > 0 and roll < 45 :
        servoHeadRoll.ChangeDutyCycle(7.0-2.0/45*roll)
        return 7.0+2.0/45*roll
    elif roll <0 and roll > -45 :
        servoHeadRoll.ChangeDutyCycle(7.0-2.0/45*roll)
        return 7.0+2.0/45*roll
    elif roll > 45 :
        servoHeadRoll.ChangeDutyCycle(7.0-2.0)
        return 9.0
    elif roll < -45 :
        servoHeadRoll.ChangeDutyCycle(7.0+2.0)
        return 5.0

    
def getFoot(foot):
    if foot > 0 and foot < 45 :
        servoFoot.ChangeDutyCycle(7.0+2.0/45*foot)
    elif foot <0 and foot > -45 :
        servoFoot.ChangeDutyCycle(7.0+2.0/45*foot)
    elif foot > 45 :
        servoFoot.ChangeDutyCycle(7.0+2.0)
    elif foot < -45 :
        servoFoot.ChangeDutyCycle(7.0-2.0)
    
def getRequest(swimMode):
    response = requests.get(
        'http://munro.local:1337',
        params={'dc':swimMode})
    try:
        pprint.pprint(response.json())
    except:
        sys.stderr.write("[receiver.py] : GETリクエスト{dc:%d}\n" % swimMode)
             
while True:
    jsonData=json.loads(sf.readline())
    if jsonData['type'] == "fliper" :
        swimMode=jsonData['swimMode']
        if swimMode != preSwimMode :
            sys.stderr.write("[receiver.py] : swimMode=%d\n" % swimMode)
            getRequest(swimMode);
            preSwimMode=swimMode        
   
    elif jsonData['type'] == "hmd" :
        getServoRoll(jsonData['roll'])
        getFoot(jsonData['roll'])
        getServoPitch(jsonData['pitch'])
        

            

                                

                                          
