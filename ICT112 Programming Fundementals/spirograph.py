# Spirograph- Vatslav Zhdanovich [1160737] 17-3-2024 

import turtle
import time
alex = turtle.Turtle()   # Birth of Alex 
wn = turtle.Screen()

# Colours
colorList = ['red','orange','yellow',
              'light green','green','navy blue',
              'blue','indigo','dark orchid',
              'orchid','magenta','orchid',
              'dark orchid','indigo','blue',
              'navy blue','green','light green',
              'yellow','orange','red']

# set speed
alex.reset()
alex.speed(100)

# Drawing shapes
for i in range(21):
    alex.penup()
    alex.left(15)
    alex.forward(30+(i*.75))
    alex.pendown()
    alex.color(colorList[i])
    alex.fillcolor(colorList[i])
    alex.begin_fill()
    for n in range(3):
         alex.left(120)
         alex.forward(100+i)
         alex.left(120)
    alex.end_fill()
time.sleep(3)

