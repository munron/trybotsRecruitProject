#書きかけ、特に利用しない
# -*- coding: utf-8 -*-
import json
import os
import sys
import time
import RPi.GPIO as GPIO
import signal


#Ctr-Cイベントハンドラ
def exit_handler(signal, frame):
    print("\nExit")
    servoHeadYaw.stop()
    servoHeadPitch.stop()
    servoFoot.stop()
    GPIO.cleanup()
    sys.exit(0)
    

"""
signal.signal(signal.SIGINT, exit_handler)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
servoHeadYaw = GPIO.PWM(17, 50)
servoHeadPitch = GPIO.PWM(22, 50)
servoFoot = GPIO.PWM(27, 50)
servoHeadYaw.start(0.0)
servoHeadPitch.start(0.0)
servoFoot.start(0.0)
"""

while True:
    try:
        jsonData=json.loads(raw_input())
        
        if jsonData['type'] == "fliper" :
            sys.stdout.write("\r%d\n" % jsonData['swimMode'])
        elif jsonData['type'] == "hmd" :
            sys.stdout.write("\rpitch : %d" % jsonData['pitch'])
            #print "roll : " + str(jsonData['roll'])
        sys.stdout.flush()
            
    except:
        sys.stderr.write( "[controller.py] JSONのパースに失敗\n")
        sys.stderr.write( "[controller.py] 終了\n")


        

    

    
    
