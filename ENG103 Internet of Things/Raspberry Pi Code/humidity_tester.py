from datetime import datetime
print(datetime.now())
print("JJ Hawkswood, Adam Weldon, Brendan Olsen, Vatslav Zhdanovich")
print("Humidity")
print('------------------------------------------------------------')

import RPi.GPIO as GPIO
import time

import Adafruit_DHT
readingNum= 0
humidList= []
tempList= []
### Loop ###
while readingNum != 6:
    dht_sensor = Adafruit_DHT.DHT11
    pin = 4
    readingNum+= 1
    seconds= readingNum * 10
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor,pin)
    # integers #
    humidityINT = int(humidity)
    secondsINT= int(seconds)
    temperatureINT = int(temperature)
    time.sleep(10)
    print('Time:', secondsINT , 'seconds')
    print ('The temperature is:', temperatureINT , 'Celsius' , temperatureINT * '*')
    print ('The humidity is:' , humidityINT , '%' , humidityINT * '*')
    humidList.append(humidityINT)
    tempList.append(temperatureINT)
print(humidList)
print(tempList)

    

    


