from datetime import datetime
print(datetime.now())
print("JJ Hawkswood, Adam Weldon, Brendan Olsen, Vatslav Zhdanovich")
print("heartbeat")
print('------------------------------------------------------------')
import Adafruit_MCP3008
import time
CLK= 11
MISO= 9
MOSI= 10
CS= 8
List=[]
mcp= Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
#print('Reading MCP3008 values, press CTRL+C to quit.')
#print('|{0:>4}|{1:>4}|{2:>4}|{3:>4}|{4:>4}|{5:>4}|{6:>4}|{7:>4}|'.format(*range(8)))
#print('-'* 57)
x=0
while x <= 99:
    values= [0]*8
    for i in range(1):
        values[i]= mcp.read_adc(i)
        #print('|{0:>4}'.format(*values))
        stars= values[i]/10
        time.sleep(.1)
        x+=1
        List.append(values[i])
        print('Time =',x/10,'sec','Sensor output:',values[i],'*'*int(stars))