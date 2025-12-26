Project: Raspberry Pi Code
Term: Semester 2 2023 (Jul - Nov)
---------------------------------------

This project contains a collection of Python scripts allowing Raspberry Pi 3 to interface with various external hardware components connected to Breadboard via the GPIO Pins. 

Distance_thing - Proximity sensor measures depth and illuminates LEDs (4 total) according to object distance from sensor (e.g. No object detected = No LEDs, object in medium range = 2 LED).

Heartbeat - Pulse and Oximeter sensor (MAX30102) measures user's heartrate and blood oxygen level. Sensor connected to MCP3008 chip on breadboard, then transmits reading to RBPi. Performs 10-seconds test and visualises pulse amplitude in terminal using asterisks (*). This implementation was particularly difficult as the sensor was designed to me used with Arduino hardware, but with modifcations done to the code the it was able to interface with the RBPi.

humidity_tester  - Humidity/Temperature sensor (DHT11) measures and prints air temp and humidity for ~1 minute, pausing for 10 seconds between readings.

LED_lights - 4 LEDs display number using 4-bit binary system. For example, to display the number 3, the last two LEDs are illuminated (0011), number 7 (0111). So for the number 10, the first and third LEDs illuminate (1010)

led_test - Tests LED function, turning on for 10 seconds before turning off. Simple program to test if LED, Breadboard and GPIO functions correctly.

Servo - Small motor performs full range-of-motion, sweeping from minimum to maximum position.

test code for Max30102 - Code for Max30102 Pulse Oximeter. Original code is for Arduino boards, so codebase was formatted manually. Needs to be 

Twilio_distance - Proximity sensor measures depth, sends SMS message using Twilio if an object is within 20cm from the sensor. For privacy and reasons, I have replaced the API keys and phone numbers (from,to) with four asterisks


