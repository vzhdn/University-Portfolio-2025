from gpiozero import Servo
from time import sleep
print("JJ Hawkswood, Brendan Olsen, Vatslav Zhdanovich")
print("Heartbeat/Oxyegen tester")
print('------------------------------------------------------------')

servo = Servo(4)

try:
    while True:
        servo.min() # Servo moves to minimum position
        sleep(0.1)
        servo.max() # Servo moves to maximum position
        sleep(0.1)
except KeyboardInterrupt:
    print("Program stopped")
