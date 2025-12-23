from datetime import datetime
print(datetime.now())
print("JJ Hawkswood, Adam Weldon, Brendan Olsen, Vatslav Zhdanovich")
print("Distance")
print('------------------------------------------------------------')

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
def measure():
    GPIO.setmode(GPIO.BCM)
    GPIO_TRIGGER =18
    GPIO_ECHO = 24
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GPIO_ECHO)== 0:
        startTime = time.time()
    while GPIO.input(GPIO_ECHO)== 1:
        StopTime = time.time()
    timeElapsed = StopTime - StartTime
    distance = (timeElapsed * 34300)/2
    print("Measured distance = %.1f cm" % distance)
    return distance
    GPIO.cleanup()
    
def closest():
    GPIO.setmode(GPIO.BCM)
    led_pin1 = 6
    led_pin2 = 13
    led_pin3 = 19
    led_pin4 = 26
    GPIO.setup(led_pin1, GPIO.OUT)
    GPIO.setup(led_pin2,GPIO.OUT)
    GPIO.setup(led_pin3,GPIO.OUT)
    GPIO.setup(led_pin4,GPIO.OUT)
    GPIO.output(led_pin1, True)
    GPIO.output(led_pin2, False)
    GPIO.output(led_pin3, False)
    GPIO.output(led_pin4, False)
    time.sleep(10)
    GPIO.cleanup()

def close():
    GPIO.setmode(GPIO.BCM)
    led_pin1 = 6
    led_pin2 = 13
    led_pin3 = 19
    led_pin4 = 26
    GPIO.setup(led_pin1,GPIO.OUT)
    GPIO.setup(led_pin2,GPIO.OUT)
    GPIO.setup(led_pin3,GPIO.OUT)
    GPIO.setup(led_pin4,GPIO.OUT)
    GPIO.output(led_pin1, True)
    GPIO.output(led_pin2, True)
    GPIO.output(led_pin3, False)
    GPIO.output(led_pin4, False)
    time.sleep(10)
    GPIO.cleanup()

def further():
    GPIO.setmode(GPIO.BCM)
    led_pin1 = 6
    led_pin2 = 13
    led_pin3 = 19
    led_pin4 = 26
    GPIO.setup(led_pin1,GPIO.OUT)
    GPIO.setup(led_pin2,GPIO.OUT)
    GPIO.setup(led_pin3,GPIO.OUT)
    GPIO.setup(led_pin4,GPIO.OUT)
    GPIO.output(led_pin1, True)
    GPIO.output(led_pin2, True)
    GPIO.output(led_pin3, True)
    GPIO.output(led_pin4, False)
    time.sleep(10)
    GPIO.cleanup()
    
def furthest():
    GPIO.setmode(GPIO.BCM)
    led_pin1 = 6
    led_pin2 = 13
    led_pin3 = 19
    led_pin4 = 26
    GPIO.setup(led_pin1,GPIO.OUT)
    GPIO.setup(led_pin2,GPIO.OUT)
    GPIO.setup(led_pin3,GPIO.OUT)
    GPIO.setup(led_pin4,GPIO.OUT)
    GPIO.output(led_pin1, True)
    GPIO.output(led_pin2, True)
    GPIO.output(led_pin3, True)
    GPIO.output(led_pin4, True)
    time.sleep(10)
    GPIO.cleanup()
    
distances= int(measure())
    
def measurment():
    if distances <= 20:
        closest()
    elif 20 != distances > 30:
        close() 
    elif 30 != distances <= 40:
        further()
    else:
        furthest()

measurment()