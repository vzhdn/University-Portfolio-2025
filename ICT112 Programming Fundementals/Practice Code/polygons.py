# Polygons- Vatslav Zhdanovich [1160737] 17-3-2024 
import turtle
import time
sizeS= int(input('What size would you like the square to be?'))
sizeT= int(input('What size would you like the triangle to be?'))
sizeH= int(input('What size would you like the hexagon to be?')) # Requesting number from user
alex= turtle.Turtle()
wn= turtle.Screen()

# Draw Square

for i in range(4):
  alex.forward(sizeS)
  alex.left(90)
  alex.forward(sizeS)
time.sleep(3)

# Draw Triangle 
for i in range(3):
  alex.forward(sizeT)
  alex.left(120)
  alex.forward(sizeT)
time.sleep(3)

# Draw Hexagon
alex.pensize(5)
for i in range(6):
  alex.forward(sizeH)
  alex.left(60)
  alex.forward(sizeH) 

time.sleep(3)
