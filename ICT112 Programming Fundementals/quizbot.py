import time
# Score 
score= 0

# Questions
questionList= {1:'What type of language is Python?',
               2:'What does the abreviation "AI" stand for?',
               3:'What type of variable is the following: x= input(int)',
               4:'What number is assigned to the first item in a list?',
               5:'What is the built-in Python module used to draw shapes? '}

# Answers
answerDict= {1:['object oriented','object based'],
             2:'artificial intelligence',
             3:'integer',
             4:['0', 'zero'],
             5:'turtle'}

print('Hello, what is your name?')
name= input()
print(f'Hi {name}!')
time.sleep(1.3)
print('Lets play a quiz game!')
time.sleep(1.3)

# Main loop
for n in questionList:
    i= n
    print(questionList[i])
    answer= input()
    if answer.lower() in answerDict[i]:
        print('Correct! +1 point')
        score= score+1
        time.sleep(1.3)
    else:
        print(f'Incorrect. The correct answer was: {answerDict[i]}')
        time.sleep(1.3)

# After questions answered, prints user results
if score >= 3:
    print(f'Congratulations {name}! You passed with a score of {score}')
else:
    print(f'Sory, {name}. You failed with a score of {score}')

