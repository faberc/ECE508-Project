# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:21:33 2020

@author: Chuck
"""


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)

print ("LED On")

GPIO.output(18, GPIO.HIGH)

time.sleep(5)

print ("LED off")

GPIO.output(18, GPIO.LOW)