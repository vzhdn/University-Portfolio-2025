from roomDescriptions import *

room_list= {}
class Room:
    ''' task ID: should be formatted like this...
                        name + direction + floor
                        So the north hallway on the second floor would be: hallNorthB1
                        Where B1 stands for 'Building 1' 
                        This is done so you can 
        name(str): Name of room 
        building(str): Building number (formatting as outlined above)
        items(list): player pickups found in room 
        tasks(dict): tasks player can interact with
        nesw(dict): available paths between rooms. If the room is unique, ignore formatting.  '''
    
    def __init__(self,
                 room_id:str,
                 name:str,
                 items:list,
                 task:str,
                 task_key:str,
                 paths:dict,
                 locked:bool
                 ): 
        
        # Define object variables
        self.name= name 
        self.room_id= room_id  
        self.items= items  
        self.task= task    
        self.task_key= task_key
        try:
            self.task_hint=self.task_key[self.task]
        except:
            self.task_hint= 'There is no task'
        self.task_status= False     # set to True after task is complete
        self.paths= paths
        self.locked= locked
        self.desc= room_desc[room_id]
        
      # Add room object to list of objects
        room_list[self.room_id]= self

#----------     Defining rooms      -----------#
# Outside
outside=Room('outside','outside',[],None,None,{'east':'entranceB2','south':'theRiseB1'},False)
#----------     Building 1 Rooms    -----------#

# Computer Lab: laptop for exam in here
computerLabB1=Room('computerLabB1','Computer Lab',['laptop'],'raspberry pi','laptop',{'west':'hallSouthB1'},False)
# Nursing Lab: Defibrillator
nursingLabB1=Room('nursingLabB1','Nursing Lab',['defibrillator'],'test dummy','defibrillator',{'east':'hallSouthB1'},False)
# Kitchen: has janitor that gives keycard
kitchenB1=Room('kitchenB1','kitchen',['empty bottle'],'janitor','coffee',{'south':'hallEastB1'},False)
# Library: geek gives you cheat sheet
libraryB1=Room('libraryB1','library',[],'geek','defibrillator',{'east':'theRiseB1','south':'hallWestB1'},False)
# Janitor Closet
janitorClosetB1=Room('janitorClosetB1','janitor closet',['mop'],None,None,{'east':'hallNorthB1'},True)
# The Rise# has map item that may or may not work
theRiseB1=Room('theRiseB1','The Rise',['map'],None,None,{'north':'outside','east':'cafeB1','south':'hallNorthB1','west':'libraryB1'},False)
# Cafe: has coffee for janitor
cafeB1=Room('cafeB1','cafe',['coffee'],None,None,{'west':'theRiseB1'},False)

#---------      Building 1 Halls    -----------#

# Centre hall, connecting other halls in building 1
hallMidB1=Room('hallMidB1','hall intersection',[],None,None,{'north':'hallNorthB1','east':'hallEastB1','south':'hallSouthB1','west':'hallWestB1'},False)
# Hall in northern direction
hallNorthB1=Room('hallNorthB1','north hall ',[],'closet','keycard',{'north':'theRiseB1','south':'hallMidB1','west':'janitorClosetB1'},False)
# Hall in eastern direction
hallEastB1=Room('hallEastB1','east hall',[],None,None,{'north':'kitchenB1','west':'hallMidB1'},False)
# hall in southern direction
hallSouthB1=Room('hallSouthB1','south hall',[],None,None,{'north':'hallMidB1','east':'computerLabB1','west':'nursingLabB1'},False)
# hall in western direction
hallWestB1= Room('hallWestB1','west hall',[],'water fountain','empty bottle',{'north':'libraryB1','east':'hallMidB1'},False)

#---------      Building 2 Rooms     -----------#
#   Entrance to building A4
entranceB2= Room('entranceB2','A4 entrance',[],None,None,{'east':'hallB2','west':'outside'},False)
#   Hall connecting entrance to the rest: has puddle for player to clean to gain access
hallB2= Room('hallB2','hall',[],'puddle','mop',{'north':'mathLabB2','west':'entranceB2','south':'theRestB2'},False)
#  Math class room: has calculator
mathLabB2=Room('mathLabB2','Math Lab',['calculator'],'equation','calculator',{'south':'hallB2'},False)
# The rest: blocked by puddle
theRestB2= Room('theRestB2','The Rest',[],'water fountain','empty bottle',{'east':'examRoomB2','north':'hallB2'},True)
#   exam room: the objective roomx
examRoomB2= Room('examRoomB2','exam room',[],'quiz','laptop',{'east':'hallB2','west':'outside'},False)

spawn_rooms=[computerLabB1,nursingLabB1,mathLabB2]