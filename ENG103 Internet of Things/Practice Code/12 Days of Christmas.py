from datetime import datetime
### Header ###
print(datetime.now())
print('Student name: Vatslav Zhdanovich\n'
      '---------------------------------\n'
### 12 days of christmas   ###
      ' Twelve days of Christmas\n')
gifts= ['And a partridge in a pear tree,',
        'Two turtle doves,',
        'Three French hens,',
        'Four calling birds,',
        'Five golden rings,',
        'Six geese a-laying,',
        'Seven swans a-swimming,',
        'Eight maids a-maiding',
        'Nine ladies dancing,',
        'Ten landlords a-leeping,',
        'Eleven pipers piping,',
        'Twelve drummers drumming,',
  ]

day= ['first',
      'second',
      'third',
      'fourth',
      'fifth',
      'sixth',
      'seventh',
      'eighth',
      'ninth',
      'tenth',
      'eleventh',
      'twelfth',
       ]
dayNum=0
while dayNum < 12:
  if dayNum== 0:
    print('On the',day[dayNum],'of Christmas,\n'
          'My true love gave to me.\n'
          'A partridge in a pear tree \n')
    dayNum+= 1
  for i in range(0,11):
    print('On the',day[dayNum],'of Christmas,\n'
          'My true love gave to me.')
    date= gifts[dayNum::-1]
    print(*date,sep='\n')
    print('\n')
    
    dayNum+= 1

  
