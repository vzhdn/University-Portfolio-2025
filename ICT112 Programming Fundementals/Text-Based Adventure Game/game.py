# Text-based adventure game #
import os
import random
import time
from roomData import *
from gameCode import *

gameStart= False     # set to false. Will be set true when user enters 'start'

#######      Functions used throughout game        #########

def clear():
    ''' Clear terminal between messages '''
    os.system('cls')

def wait(n):
    ''' Allows for waiting between commands/statements '''
    time.sleep(n)

def action(cmd):    
    ''' Command handler '''
    if not cmd: # handle empty inputs
            print('Cannot be empty')

    if cmd[0]== 'quit':
        quit()
    elif cmd[0] == 'help':
        MenuHelp()
    elif cmd[0] == 'hint':
        hint()
    elif len(cmd)== 1:        # if command has no subject, pass
        print('Invalid command')
        pass
    else:
        match cmd[0]:
            
                # go, head or walk: Movement between room 
                case 'go'|'head'|'walk' :
                    player.move(cmd)

                # about or inspect: Request description
                case 'about'|'inspect':
                    player.about(cmd)
                        
                # take, grab or pickup: Take item from room
                case 'take'|'grab'|'pickup':
                    if len(cmd) == 2:   # if input item is only one word
                        item= cmd[1]
                        player.take(item)
                    elif len(cmd) > 2:  # if input item is two words
                        item=' '.join(cmd[1:])
                        player.take(item)

                # drop: Drop item from inventory
                case 'drop':
                    item= cmd[1]
                    player.drop(item)

                # use: Use item if in inventory or room 
                case 'use':
                    item= cmd[1:]
                    player.use(item)

                # Response to unrecognised commands
                case _:
                    print('Invalid command')

def MenuHelp():
    print("This game follows strict spelling. You must spell items exactly as they are written/described\nYou control your character by typing things on the keyboard.")
    print("Commands:\n     go/head/walk <compass direction> | Move between rooms\n     inspect/about <object, item, me> |  Description of object or item. If command me, shows name, inventory, room and score.\n     take/grab/pickup <item> | Take item\n     drop <item> | Drop item from inventory\n     use <item or object> | Use item or object.\n     help | Show commands\n     hint | Use 5 points to get hint\n     quit | Quit program")   

def hint(): 
    if player.room.task is None:
        print('There is no task here')
    elif player.score < 5:
         print('You do not have enough points.')
    else:
        print(f'Using a hint costs you -5 points off your final score\n Get hint?')
        choice= input("Type yes or no: ")
        if choice=='yes':
            player.score -+ 5
            print(f"You need to use the {player.room.task_key} on the {player.room.task}")
        else:
            pass         

def menu():
    ''' print main menu text and handle main menu inputs '''
    global gameStart   
    player_room= random.choice(spawn_rooms) # set player's room to random room out of three choices
    player_room.locked= True    # Lock room so player must 
    MenuHelp()
    while gameStart== False:    # if gameStart
        cmd= input('Type "start" to begin game:').lower().split()   #lower words and split input into list
        if cmd[0] == 'start':
            clear()
            player_name= input('Greetings! Enter name:')    # Request player's name
            player= Player(player_name,player_room,[])    # Create player
            gameStart= True                                 # Set gameStart to True for main loop
            clear()
                # intro
            print(f"You are just finishing you lesson in the {player.room.name}.\n'Alright everyone, it's almost the end of the lesson. \n'Wrap up what you're working on and get out.")
            wait(2)
            print(f"Before you start the exam, you need to make sure you take your laptop, and a drink with you.\n Your laptop is in the computer lab, in building A1. ")
            print(f'You are in the {player.room.name}')
            print('--------Room-----------')
            player.about(['about','room']) # describe players room
            return player
        else:
            pass

def mainLoop():
    '''  Main loop: Prompt player for input. Lowering and splitting input before passing to action handler  '''
    while examRoomB2.task_status == False:    # While exam hasn't been done
        print('-------Command---------')
        cmd= input('Enter command:').lower().split()
        if not cmd: # handle empty inputs
            print('Cannot be empty')
            continue
        clear()
        print('-------Result---------')
        action(cmd) # pass input to action handler
        print('--------Room-----------')
        player.about_room()
        # Check if exam is complete
    if examRoomB2.task_status == True:
        clear()
        if 'cheatsheet' in player.inv:
            player.score += 100
            print(f'Using the cheatsheet, you get an A grade.\n  Congratulations! You beat the game!\n Final score:{player.score}')
        else:
            grade= player.score
            if grade >= 85:
                print('  ~ You completed the quiz with an A grade. Congratulaions!!! ~  ')
                print(f'Final score:{player.score}')
            elif grade >= 40 < 85:
                print('  ~ You completed the quiz with an B grade. Congratulaions! ~  ')
                print(f'Final score:{player.score}')
            elif grade >=25 <40:
                print("  ~ You completed the quiz with an C grade. It's technically a pass.  ")
                print(f'Final score:{player.score}')
            elif grade >= 10 <25:
                print('  ~ You completed the quiz with an D grade :-(   ~  ')
                print(f'Final score:{player.score}')
            elif grade < 10:
                print(' Despite your best efforts, you failed the exam. Better study next time')
                print(f'Final score:{player.score}')
    else:
        pass

###########        Main loop           ################
clear() 
player= menu()
mainLoop()


