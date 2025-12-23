
import RPi.GPIO as GPIO
import time
print("JJ Hawkswood, Brendan Olsen, Vatslav Zhdanovich")
print("Heartbeat/Oxyegen tester")
print('------------------------------------------------------------')
GPIO.setmode(GPIO.BCM)
led_pin= 14
GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(led_pin, True)
time.sleep(10)
GPIO.output(led_pin, False)
GPIO.cleanup()

# LED pin socket numbers:  14 16 18 24 #
def class led
  self.Name= 'Name'
  self.Pin= int
  led_one= bool
  led1= 14
  GPIO.setup(led1, GPIO.OUT)
  if led_one == True:
    GPI.output(led1, True)
  else:
    GPI.output(led1,False)

    


def zero():
  led_one(False)
  

led_one(True)
