from datetime import datetime
import time
import random
### Header ###
print(datetime.now())
print('Student name: Vatslav Zhdanovich')
print('----------------------------------')
print('DICE THROW!')
time.sleep(2)
print('This state-of-the-art program simulates throwing 2 dice')
print('----------------------------------')
print(' ')
time.sleep(2)
t2= 0
t3= 0
t4= 0
t5= 0
t6= 0
t7= 0
t8= 0
t9= 0
t10= 0
t11= 0 
t12= 0
n= int(input('How many times would you like to throw the dice?'))
print('Throwing!')
for i in range(0,n):
    dthrow= random.randint(2,12)
    if dthrow== 2:
        t2= t2 + 1
    elif dthrow== 3:
        t3= t3 + 1
    elif dthrow== 4:
        t4= t4 + 1
    elif dthrow== 5:
        t5= t5 + 1
    elif dthrow== 6:
        t6= t6 + 1
    elif dthrow== 7:
        t7= t7 + 1
    elif dthrow== 8:
        t8= t8 + 1
    elif dthrow== 9:
        t9= t9 + 1
    elif dthrow == 10:
        t10= t10 + 1
    elif dthrow == 11:
       t11= t11 + 1
    else:
        t12= t12 + 1
time.sleep(2)
print('The total times 2 was rolled: ' + str(t2))
print('The total times 3 was rolled: ' + str(t3)) 
print('The total times 4 was rolled: ' + str(t4))
print('The total times 5 was rolled: ' + str(t5)) 
print('The total times 6 was rolled: ' + str(t6))
print('The total times 7 was rolled: ' + str(t7)) 
print('The total times 8 was rolled: ' + str(t8))
print('The total times 9 was rolled: ' + str(t9))
print('The total times 10 was rolled: ' + str(t10))
print('The total times 11 was rolled: ' + str(t11))
print('The total times 12 was rolled: ' + str(t12))
 



