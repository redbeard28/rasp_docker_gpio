#!/usr/bin/python3
#encoding:utf-8
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Jeremie CUADRADO <redbeard28>

import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
LED_PIN = 11
GPIO.setup(LED_PIN,GPIO.OUT)

def blink():
    GPIO.output(LED_PIN,GPIO.HIGH)
    time.sleep(0.5)    
    GPIO.output(LED_PIN,GPIO.LOW)
 
if __name__ == '__main__':
    try:
        while True:
            time.sleep(0.5)
            blink()
    except:
        print("Bye!")
        GPIO.cleanup()
