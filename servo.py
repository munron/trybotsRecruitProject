# -*- coding: utf-8 -*-
import json
import sys
import RPi.GPIO as GPIO
import time
import signal  

arg=sys.argv
print arg
print str(len(arg))
parameter=0;

#Ctr-Cイベントハンドラ
def exit_handler(signal, frame):
  print("\nExit")
  servo_head.stop()
  servo_tail.stop()
  servo_foot.stop()
  GPIO.cleanup()
  sys.exit(0)

#終了時処理
def exit():
  print("\nExit")
  servo_head.stop()
  servo_tail.stop()
  servo_foot.stop()
  GPIO.cleanup()
  sys.exit(0)
  

 

#サーボモーターセットアップ
signal.signal(signal.SIGINT, exit_handler)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
servo_head = GPIO.PWM(17, 50)
servo_tail = GPIO.PWM(22, 50)
servo_foot = GPIO.PWM(27, 50)
servo_head.start(0.0)
servo_tail.start(0.0)
servo_foot.start(0.0)

while True:
  signal=float(raw_input())
  if signal==1 :
    parameter=json.loads(open('setting.txt').read())
    print parameter['forward_head']
    print parameter['forward_tail']
    print parameter['forward_foot']
    servo_head.ChangeDutyCycle(int(parameter['forward_head']))
    servo_tail.ChangeDutyCycle(int(parameter['forward_tail']))
    servo_foot.ChangeDutyCycle(int(parameter['forward_foot']))
    time.sleep(0.2)
  
    
  if signal==2 :
    parameter=json.loads(open('setting.txt').read())
    print parameter['left_head']
    print parameter['left_tail']
    print parameter['left_foot']
    servo_head.ChangeDutyCycle(int(parameter['left_head']))
    servo_tail.ChangeDutyCycle(int(parameter['left_tail']))
    servo_foot.ChangeDutyCycle(int(parameter['left_foot']))
    time.sleep(0.2)


  if signal==3 :
    parameter=json.loads(open('setting.txt').read())
    print parameter['dive_head']
    print parameter['dive_tail']
    print parameter['dive_foot']
    servo_head.ChangeDutyCycle(int(parameter['dive_head']))
    servo_tail.ChangeDutyCycle(int(parameter['dive_tail']))
    servo_foot.ChangeDutyCycle(int(parameter['dive_foot']))
    time.sleep(0.2)
    
  
  if signal==4 :
    parameter=json.loads(open('setting.txt').read())
    print parameter['right_head']
    print parameter['right_tail']
    print parameter['right_foot']
    servo_head.ChangeDutyCycle(int(parameter['right_head']))
    servo_tail.ChangeDutyCycle(int(parameter['right_tail']))
    servo_foot.ChangeDutyCycle(int(parameter['right_foot']))
    time.sleep(0.2)

  if signal==5 :
    exit()  
  
