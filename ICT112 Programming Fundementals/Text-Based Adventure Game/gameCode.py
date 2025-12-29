### Main code for Task 3 Text-Based adventure game ###
from roomData import *
from roomDescriptions import *
import time
import os
from PIL import Image

def clear():
    ''' Clear terminal between messages '''
    os.system('cls')

class Player():
    ''' Player class '''

    def __init__(self,name,room,inv,):
        
        self.name= name
        self.room= room
        self.inv= inv
        self.score= 0   # player score determined by completing tasks 
    
    #   Movement handler    #
    def move(self,cmd):
        ''' Movement handler: changes player's room to one in desired direction if found in zonemap variable'''
        global room_list
        direction= cmd[1]   # direction is the second word of the command

        if direction in self.room.paths: # if direction in zonemap of players current room
            new_room= room_list.get(self.room.paths[direction]) # new_room is the room that in the direction selected by player
           
            if self.room.locked or new_room.locked == True: # If room is locked, dont let them leave/enter 
                if new_room is theRestB2:
                    print(f'The puddle is too wide to jump. You cannot enter the {new_room.name}')
                else:
                    print(f"The door is locked. You cannot enter the {new_room.name}")
            else:
                self.room= new_room
                print(f"You go {direction} and enter the {self.room.name}.") # print player's current room

        else:
            print(f'You cannot go {direction}.')

    #   Take item   #
    def take(self,item):
        '''  If item present in current room, add to player's inventory and remove from room's item list   '''

        if item in self.room.items:
            if len(self.inv) == 3:  # if player is carrying 3 items, dont let them pick up requested item
                print(f"You do not have any space in your inventory.\nDrop something pick up the {item}. ")
            else:
                print(f"You take the {item}.")
                self.room.items.remove(item)
                self.inv.append(item)
        elif item in self.inv:
            print(f"You already have the {item}.")
        else:
            print(f"You cannot take the {item}.")

    #   Drop item   #
    def drop(self,item):
        '''  If item present in player's inventory, add to room's item list and remove from player's inventory  '''

        if item in self.inv:
            print(f'You drop the {item}.')
            self.inv.remove(item)
            self.room.items.append(item)
        else:
            print(f'You do not have a {item} to drop.')

    #   Use item/object  #
    def use(self,cmd):
        '''  If item/object is in either the player's inventory, is current room's key item, or is object in room, try to print associated
             text from roomDescriptions.py. Also changes room.task_status if item used is room.task_key '''
        
        if len(cmd)== 1:    # if item to use is only one word
            self.use_checkcmd(cmd)
        elif len(cmd) > 1: 
            cmd= ' '.join(cmd)
            if cmd== self.room.task:
                try:
                    print(task_use[cmd])
                except:
                    print(f'Cannot use the {cmd}')
            elif cmd== self.room.task_key and cmd in self.inv:
                print(item_use[cmd][self.room.task])
                if cmd== 'empty bottle':
                    self.inv.remove('empty bottle')
                    self.inv.append('water bottle')

            else:
                print(f'Cannot use the {cmd}')

    #   About item/object #
    def about(self,cmd):
        ''' Provide description of input if it exists in roomDescriptions.py '''

        try:
            if len(cmd) == 2:   # if input has two words i.e: about laptop
                match cmd[1]:   # match the second word to one of the cases
                    case 'me':
                        self.about_me()
                    case 'room':
                        self.about_room()
                    case _:     # if input is neither 'me' or 'room'
                        try:
                            print(desc[cmd[1]]) # try finding second word in 'desc' dictionary
                        except:
                            print(f"There's nothing interesting about the {cmd[1]}") # if no such item found, print error
            elif len(cmd) > 2:  # if input has more than two words i.e: about raspberry pi
                cmd_formatted= ' '.join(cmd[cmd.index(cmd[1]):cmd.index(cmd[1]) + 2])   # combine the second and third word
                try:
                    print(desc[cmd_formatted])
                except:
                    print(f"There's nothing interesting about the {cmd_formatted}.")
        except:
            print('Error: About error')
    
    #   About player
    def about_me(self):
        '''  Provides brief description of player's current state '''
        room= self.room.name
        inventory_text = ', '.join(self.inv)
        print(f'Your name is {self.name} \nYou are currently in the {room}. \nYou have a {inventory_text} in your inventory.\n Your score: {self.score}')
    
    #   About player's room
    def about_room(self):
        '''  Prints brief description of player's surroundings  '''
        print(f'Room description:\n{self.room.desc}') # print description of player's room

        if self.room.task_status== True:    # if task has been completed
            print(f'Task status: Completed\n{task_desc_solved[self.room.task]}')  # print description of completed task
            paths= self.room.paths.items()
            print('Paths:')
            for dir, room_id in paths:
                room_name= room_list[room_id].name
                print(f"  {dir.capitalize()} leads to the {room_name}")   # print available paths

        elif self.room.task_status== False:
            if self.room.task == None:
                paths= self.room.paths.items()
                print('Paths:')
                for dir, room_id in paths:
                    room_name= room_list[room_id].name
                    print(f"  {dir.capitalize()} leads to the {room_name}") # print available paths
            else:
                print(f'Task status: Incomplete\n{task_desc[self.room.task]}')
                paths= self.room.paths.items()
                print('Paths:')
                for dir, room_id in paths:
                    room_name= room_list[room_id].name
                    print(f"  {dir.capitalize()} leads to the {room_name}")# print available paths

        if len(self.room.items) == 0:
            print(f'Items:\n  There is nothing here to take.')
        else:
            items= ','.join(self.room.items)
            print(f"Items:\n  In the room there is a {items} ")

    #   Check use input
    def use_checkcmd(self,cmd):
        ''' Check what command is for player.use function  '''
        try:    #Try using item : perform checks to see if item is room key
            cmd= cmd[0] 
            if cmd == self.room.task_key:   # if item to use is the key for the room's task
                if cmd in self.inv:
                    if self.room.task== 'puddle':
                            print(f'You use the mop to make a path through the puddle')
                            self.score += 10
                            self.room.task_status= True
                            theRestB2.locked= False
                    elif self.room.task== 'closet':
                        print(f'You swipe the keycard on the closet door card reader. The door unlocks')
                        self.score += 10
                        janitorClosetB1.locked= False
                        self.room.task_status= True
                    elif self.room.task== 'geek':
                            print(f'You present the defibrillator to the geek.\n  Without breaking eye contanct with the computer, he quietly takes the defibrillator from you\n and hands you the cheatsheet.')
                            self.score += 15
                            self.inv.remove(cmd[0])
                            self.inv.append('cheatsheet')
                            self.room.task_status= True
                    elif self.room.task== 'janitor':
                            print(f"You present the coffee to the janitor.\n  'Thanks mate, you're a life saver. Heres that keycard I promised'")
                            self.score += 10
                            self.inv.remove('coffee')
                            self.inv.append('keycard')
                            self.room.task_status= True
                    elif self.room.locked == True:
                        print(f"You use the {cmd} on the {self.room.task}")
                        print(item_use[cmd][self.room.task])
                        self.score += 10
                        self.room.task_status= True
                        self.room.locked = False
                    elif self.room.locked== False:
                        if self.room== examRoomB2:
                            if 'laptop' and 'water bottle' not in self.inv:
                                print("You can't start the quiz without a laptop and water bottle in your inventory.")
                            else:
                                print(f"You use the {cmd} on the {self.room.task}")
                                print(item_use[cmd][self.room.task])
                                time.sleep(3)
                                print('The exam was harder than you expected.')
                                self.room.task_status= True
                        else:
                            print(f"You use the {cmd} on the {self.room.task}")
                            print(item_use[cmd][self.room.task])
                            self.score += 10
                            self.room.task_status= True

                else:
                    print(f'You do not have the {cmd}.')
            elif cmd[0] == self.room.task:  #if use item is the room task
                if self.room.task== 'water fountain' and 'empty bottle' in self.inv:
                    del self.inv['empty bottle']
                    self.inv.append('water bottle')
                try:
                    print(task_use[cmd])
                except:
                    print(f'Cannot use {cmd}.')     
            elif cmd== 'map':
                 # Open 'map' png
                 print('*  Caution: After you have looked at map, close map window to proceed with game. Game will remain frozen until map window is closed* ')
                 time.sleep(5)
                 print('You look at the map.')
                 image = Image.open("code/game_map_v4.png")
                 # Display the map
                 image.show()       

            else:
                print(f"You cannot use the {cmd[0]}.")
        except:
            print('Cannot use this here')