from datetime import datetime
print(datetime.now())
print("JJ Hawkswood, Adam Weldon, Brendan Olsen, Vatslav Zhdanovich")
print("Our first electrical disaster")
import RPi.GPIO as GPIO
import time

def zero():
    GPIO.setmode(GPIO.BCM)
    led_pin1 = 14
    led_pin2 = 16
    led_pin3 = 18
    led_pin4 = 23
    GPIO.setup(led_pin1, GPIO.OUT)
    GPIO.setup(led_pin2,GPIO.OUT)
    GPIO.setup(led_pin3,GPIO.OUT)
    GPIO.setup(led_pin4,GPIO.OUT)
    GPIO.output(led_pin1, False)
    GPIO.output(led_pin2, False)
    GPIO.output(led_pin3, False)
    GPIO.output(led_pin4, False)
    time.sleep(10)
    GPIO.cleanup()

def seven():
    GPIO.setmode(GPIO.BCM)
    led_pin1 = 14
    led_pin2 = 16
    led_pin3 = 18
    led_pin4 = 23
    GPIO.setup(led_pin1,GPIO.OUT)
    GPIO.setup(led_pin2,GPIO.OUT)
    GPIO.setup(led_pin3,GPIO.OUT)
    GPIO.setup(led_pin4,GPIO.OUT)
    GPIO.output(led_pin1, False)
    GPIO.output(led_pin2, True)
    GPIO.output(led_pin3, True)
    GPIO.output(led_pin4, True)
    time.sleep(10)
    GPIO.cleanup()

def sthree():
    GPIO.setmode(GPIO.BCM)
    led_pin1 = 14
    led_pin2 = 16
    led_pin3 = 18
    led_pin4 = 23
    GPIO.setup(led_pin1,GPIO.OUT)
    GPIO.setup(led_pin2,GPIO.OUT)
    GPIO.setup(led_pin3,GPIO.OUT)
    GPIO.setup(led_pin4,GPIO.OUT)
    GPIO.output(led_pin1, False)
    GPIO.output(led_pin2, False)
    GPIO.output(led_pin3, True)
    GPIO.output(led_pin4, True)
    time.sleep(10)
    GPIO.cleanup()

zero()
time.sleep(5)
seven()
time.sleep(5)
sthree()
time.sleep(5)
seven()
time.sleep(5)
zero()


