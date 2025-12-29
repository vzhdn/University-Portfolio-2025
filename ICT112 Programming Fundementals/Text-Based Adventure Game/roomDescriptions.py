
# Double space beginning of desc and after \n so that descriptions can be distinguished from other text 

#---------------------    ROOMS   ---------------------------------   
room_desc={#         Room descriptions       #
                      # Outside description     
            'outside':
            "  You are in the middle of the courtyard.\n  To west are buildings A2 and A3, however they are both under construction,\n There is a BBQ area next to the grass area, with some benches surrounding it.",

                      # Building 1 Descriptions: Rooms

            'computerLabB1':
              '  The room is filled with computers.\n  The hum of the florescent lights is enough to make anyone go insane.\n  On the table is a Raspberry Pi ',

            'nursingLabB1':
              "  There is a couple tables around the edges of the room, surrounding a stretcher in the middle.\n  On the stretcher lays a test dummy.\n  Next to the stretcher is a cart with various medical tools, but a defibrillator catches your eye. ",

            'janitorClosetB1':
              "  A small stoage closet, with shelves lining the walls.\n  There is an assortment of cleaning supplies and chemicals littered about.\n  A mop is sticking out a bucket next to the door",

            'libraryB1':
              "  Rows of shelves span the length of the library.\n  Along the east wall are tables and computers.\n  At one of the tables sits a stereotypical geek, staring intenly at the computer monitor.",

            'kitchenB1':
              "  A small kitchen with a shared fridge, sink and microwave. In the middle, there is an island table.\n  Behind the table sits the janitor.",

            'cafeB1':
              "  A simple cafe. There's a display fridge with all sorts of pastries. ",

            'theRiseB1':
              "  A massive hall with a great staircase in the middle.\n  Due to renovations being carries out, the staircase is inaccessible, as well as one of the halls.\n  There is a reception desk towards the north, however there is nobody present.\n  Next to the reception desk is a magazine stand, with nothing stocked but the same map of the campus.",

                      # Building 1 Descriptions: Halls

            'hallNorthB1':
              "  The northern hall. There are classrooms along the east wall, however they are all in use.\n  There is a janitor closet to the west.",

            'hallEastB1':
              "  The eastern hall. To the east is the auditorium, however it is currently being used. There are some chairs and tables to the south.",

            'hallSouthB1':
              "  The southern hall. Theres a window to the south over looking the road",

            'hallWestB1':
              "  The western hall. The hall leading to the Rise is blocked by construction equipment.\n  The elevator is out of order\n  There is a water fountain on the south wall.",

            'hallMidB1':
              "  The intersection where the halls converge.\n  The hall extends in each direction",

#---------------          Building 2          --------------------------------
                #   Building 2 Descriptions: rooms  #
        
            'entranceB2':
              "  The entrance to building A4. There is a large staircase leading to the second floor, howver there is construction blocking them",

            'mathLabB2':
              "   A typical class room, with a couple tables arranged facing towards the white board on the east wall.\n  ",

            'theRestB2':
              "  A lounge for students and staff alike.\n  A small kitchenette in the corner, with some couches and tables around the room.\n  The elevator is out of order",

            'examRoomB2':
              "  A standard classroom, with several tables arranged facing towards the tv on the south wall",

               #  Building 2 Description: halls #

               'hallB2':
              "  A short hallway. There's a corkboard on the wall with some flyers and posters.\n  A puddle is leaking into the hallway from under the barrier."
              }

#----------------   ITEMS   ----------------------------

desc= {
      #         Item desciptions        # 
            # Computer lab items
            'laptop':"  It's a generic black laptop, with various ports lining it's side.\n  Not particularly remarkable in anyway whatsoever.\n  *Required to complete game*",
            'defibrillator':"  A defibrillator, used to apply an electric charge/current to change or restore heartbeat to normal.",
            'calculator':"  It's a Texas Instrument Ti-84 CE Plus Graphing Calculator. Good for solving graphs.",
            'mop':"  It's a mop.",
            'coffee':"  A paper cup filled with coffee. It isn't very warm.",
            'map':"  A map of the USC campus. ",
            'cheatsheet':"  The cheatsheet has all the information you need for the quiz. This will guarentee you get a good grade.",
            'empty bottle':"  An empty plastic water bottle. You're pretty sure it's yours.",
            'water bottle':"  Your bottle filled with water.",
      #         Task descriptions       #
        # computer lab task
            'raspberry pi':"  The Raspberry Pi sits on the table with a red LED blinking. There is a USB cord extending from the board.\n  Maybe it could be plugged into something...",
        # nursing lab task
            'test dummy':"  The disturbingly realistic medical test dummy lays on the stretcher.\n  Upon closer inspection it appears as though the dummy's heart is arythmic... ",
            'dummy':"  The disturbingly realistic medical test dummy lays on the stretcher.\n  Upon closer inspection it appears as though the dummy's heart is arythmic... ",
        # math lab task
            'equation':"  The whiteboard reads: 'When graphed, what kind of shape does y=x^2 create?\n  Maybe you could solve the question if you had some sort of device...",
            'whiteboard':"  The whiteboard reads: 'When graphed, what kind of shape does y=x^2 create?\n  Maybe you could solve the question if you had some sort of device...",
        # west hall task
            'water fountain':  "A particularly fancy drinking foutain attched to the wall. ",

        # kitchen task
            'janitor':"  The janitor sits behind the counter looking at his phone.\n  He looks pretty tired. ",
            'geek':"  The geek is staring at the computer screen from 3 inches away.\n He looks pretty smart."
}

#----------------   TASKS    ---------------------------

task_desc={
      #         Task descriptions       #
            'raspberry pi':"  The LED on the Raspberry Pi is blinking red.",
            'test dummy':"  A test dummy is laying on the stretcher.",
            'equation':"  A single equation is written on the whiteboard.",
            'puddle':"  The puddle is originating from the toilets to the east, blocking your way to the Rest.\n  It's too wide to jump and too much of a biohazard to walk through.",
            'water fountain':"  A particularly fancy water foutain attched to the wall. ",
            'janitor':"  The Janitor asks you from across the table,\n  'Hey mate, do you think you could do me a favour?'\n  'I hardly got any sleep last night. Fetch me a coffee, will ya?'\n  'I'll give you the keycard for the janitor closet'",
            'geek':"  Without diverting his eyes from the screen the geek asks you,'I need a defibrillator for my assignment. Don't ask why'\n  'Bring one and I'll give you a cheatsheet for the exam.'",
            'closet':"  The door to the janitor closet is locked.\n  It needs a key card to open.",
            'quiz':"  The lecturer is sitting behind her table. She says to you:\n 'You still have time to complete the quiz. Just make sure you your laptop has lost of charge'.\n  'It will probably take some time, so I recommend having a drink also.'"
}

task_desc_solved={
      #         Task descriptions       #
            'raspberry pi':"  The LED on the Raspberry Pi is a steady green. The teacher let's you leave",
            'test dummy':"  The test dummy is no longer arythmic. The teacher let's you leave",
            'equation':"  'It's a parabola' is written on the whiteboard. The teacher let's you leave",
            'water fountain':"  A particularly fancy water foutain attched to the wall. ",
            'janitor':"  'Thanks for the coffee mate!'",
            'geek':'  The geek sits at the computer, typing.',
            'closet': '  The janitor closet door is unlocked',
            'puddle':"  There is a path through the puddle.",
            'quiz':"  You completed the exam!"

}
    
task_use= {
    'raspberry pi':"  You try to turn the light green by moving some wires around but it doesn't seem to work.",
    'test dummy':"  You try to fix the dummy's heart by turning the un-labled dial located on it's side, but the dummy starts convulsing.\n  You turn the dial to it's original position.",
    'puddle':"  You would rather not.",
    'water fountain':"  You take a drink of water."
    
}

#---------------- INTERACTIONS  ---------------------------------
    # Key is the item being used, the value is a dictionary with the keys being item/objects, and the values being response
    # For example: laptop:{}
item_use= {
    'laptop':{'raspberry pi':"  You take the USB cable and plug it directly into your computer. A terminal window opens for half a second before closing.\n  The red light on the board flashes rapidly before turning green.",
              'quiz':"  You open your laptop and log into Canvas\n  You begin the quiz."},
    'defibrillator':{'test dummy':"  You take both paddles in both hands before pressing them to the dummy's chest.\n  The dummy's eyes spring open."},
    'calculator':{'equation':"  You enter the equation into the calculator.\n  On the screen it returns a graph.\n  You walk up to the whiteboard, grab a marker and write next to the question.\n  'It's a parabola.'"},
    'empty bottle':{'water fountain':"  You fill the empty bottle with water from the fountain."},
}

