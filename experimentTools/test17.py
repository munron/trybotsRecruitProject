#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import signal
import sys

def exit_handler(signal, frame):
  print("\nExit")
  servo.stop()
  GPIO.cleanup()
  sys.exit(0)


signal.signal(signal.SIGINT, exit_handler)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
servo = GPIO.PWM(17, 50)
servo.start(0.0)

while True :
  dc=float(raw_input())
  print "[%f]" % dc
  servo.ChangeDutyCycle(dc)
  time.sleep(0.2)

