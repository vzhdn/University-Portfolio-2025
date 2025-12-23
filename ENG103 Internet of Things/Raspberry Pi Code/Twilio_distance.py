from datetime import datetime
print(datetime.now())
print("JJ Hawkswood, Adam Weldon, Brendan Olsen, Vatslav Zhdanovich")
print("Twilio Distance")
print('------------------------------------------------------------')

import RPi.GPIO as GPIO
import time
from twilio.rest import Client
GPIO.setwarnings(False)

#print(message.sid)

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
    return distance
    GPIO.cleanup()
    
c= 0
while c< 6:
    time.sleep(10)
    c= c+1
    t= c * 10
    distance= int(measure())
    if distance < 20:
        print('Time:',t,'secs. Distance measured is',distance,'CM. ALERT Message sent to mobile phone, program exiting')
        account_sid= '****'
        auth_token= '****'
        client= Client(account_sid, auth_token)
        message= client.messages \
             .create(
                 body='<<Brendan>>:ENG103 Distance proximity alert: Distance less than 20CM.',
                 from_='****',
                 to='****'
                 )
        break
    else:
        print('Time:',t,'secs. Distance measured is',distance,'CM. No alert')
