from datetime import datetime
### Header ###
print(datetime.now())
print("Student name: Vatslav Zhdanovich")
print("-------------------------------")
### Input ###
inputAUD = float(input('Please input amount of money:'))
### Conversions ###
moneyUSD= inputAUD * .6948
moneyEUR= inputAUD * .6150
moneyGDP= inputAUD * .5505
moneyINR= inputAUD * 52.2542
### Output ***
print("This amount would be converted to USD: " + str(moneyUSD))
print("This amount would be converted to EUR: " + str(moneyEUR))
print("This amount would be converted to GDP: " + str(moneyGDP))
print("This amount would be converted to INR: " + str(moneyINR))
