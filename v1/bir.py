import os,time
from gtts import gTTS
from pygame import mixer
from firebase import firebase
import RPi.GPIO as IO
import time,math
IO.setwarnings(False)
IO.setmode(IO.BOARD)
IO.setup(16,IO.IN) #GPIO 2 -> Left IR out
IO.setup(18,IO.IN) #GPIO 3 -> Right IR out
IO.setup(32,IO.OUT) #GPIO 4 -> Motor 1 terminal A
IO.setup(36,IO.OUT) #GPIO 14 -> Motor 1 terminal B
IO.setup(38,IO.OUT) #GPIO 17 -> Motor Left terminal A
IO.setup(40,IO.OUT)


firebase = firebase.FirebaseApplication('https://welcomebiryani-51293.firebaseio.com/', None)

matr=[];
inde=1;
rowi=0;

#------------------------------------------------------------------------------#

def voice(string):
    global inde;
    tts = gTTS(text=string, lang='en')
    tts.save("sound"+str(inde)+".mp3")
    mixer.init()
    mixer.music.load("sound"+str(inde)+".mp3")
    mixer.music.play()
    time.sleep(5)
    inde=inde+1;

#------------------------------------------------------------------------------#

def updateMatrix():
    data=''
    k=1;
    while(k==1):
        if( os.stat("buffer.txt").st_size != 0 ):
            f=open("buffer.txt","r")
            data=(str(f.read()))
            f.close()
            f=open("buffer.txt","w")
            f.write("")
            f.close()
            k=k+1;
    mat=[]        
    mat=data.split(",");
    stri=list(map(int, mat))
    #print(stri);
    matr.append(stri);
    matr.append([0,0,0,0]);
    matr.append([0,0,0,0]);
    matr.append([0,0,0,0]);
    #print(matr)
    
#------------------------------------------------------------------------------#

def fb():
    try:
        result='';
        result = result+firebase.get('/table1', None)
        i=2;
        while i<5:
            result = result+","+firebase.get('/table'+str(i), None)
            i=i+1
            #print(result)
        if("None" not in result):
            f=open("buffer.txt",'w')
            f.write(str(result))
            f.close()
    except:
        print("adsa")

#------------------------------------------------------------------------------#



def calPath(table):
    row=math.ceil(table/2);
    tab=table%2;
    print("Row number",row)

    while 1:
 
        if(IO.input(16)==False and IO.input(18)==False): #both while move forward     
            print("Straight")
            IO.output(32,True) #1A+
            IO.output(36,False) #1B-
            IO.output(38,True) #2A+
            IO.output(40,False) #2B-
            
        elif(IO.input(16)==False and IO.input(18)==True): #turn right  
            print("Right")
            if(third==True):
                rowi=rowi+1;
                if(row==rowi):
                    IO.output(32,True) #1A+
                    IO.output(36,True) #1B-
                    IO.output(38,True) #2A+
                    IO.output(40,False)#2B-

                else:
                    print("Straight")
                    IO.output(32,True) #1A+
                    IO.output(36,False) #1B-
                    IO.output(38,True) #2A+
                    IO.output(40,False) #2B-
                    
                        
            elif(third==False):
                IO.output(32,True) #1A+
                IO.output(36,True) #1B-
                IO.output(38,True) #2A+
                IO.output(40,False)#2B-
                        
        elif(IO.input(16)==True and IO.input(18)==False): #turn left
            print("Left")
            if(third==True):
                rowi=rowi+1;
                if(row==rowi):
                    if(table%2!=0):
                        IO.output(32,True) #1A+
                        IO.output(36,False) #1B-
                        IO.output(38,True) #2A+
                        IO.output(40,True)#2B-
        
        else:  #stay still
            print("Stop")
            IO.output(32,True) #1A+
            IO.output(36,True) #1B-
            IO.output(38,True) #2A+
            IO.output(40,True) #2B-

    
#------------------------------------------------------------------------------#

def goLeft():
    while 1:
     
            if(IO.input(16)==False and IO.input(18)==False): #both while move forward     
                print("Condition 1")
                IO.output(32,True) #1A+
                IO.output(36,False) #1B-
                IO.output(38,True) #2A+
                IO.output(40,False) #2B-
            elif(IO.input(16)==False and IO.input(18)==True): #turn right  
                print("Condition 2")
                IO.output(32,True) #1A+
                IO.output(36,True) #1B-
                IO.output(38,True) #2A+
                IO.output(40,False) #2B-
            elif(IO.input(16)==True and IO.input(18)==False): #turn left
                print("Condition 3")
                IO.output(32,True) #1A+
                IO.output(36,False) #1B-
                IO.output(38,True) #2A+
                IO.output(40,True) #2B-
            else:  #stay still
                print("else condition")
                IO.output(32,True) #1A+
                IO.output(36,True) #1B-
                IO.output(38,True) #2A+
                IO.output(40,True) #2B-
#------------------------------------------------------------------------------#

def goRight():
    while 1:
     
            if(IO.input(16)==False and IO.input(18)==False): #both while move forward     
                print("Condition 1")
                IO.output(32,True) #1A+
                IO.output(36,False) #1B-
                IO.output(38,True) #2A+
                IO.output(40,False) #2B-
            elif(IO.input(16)==False and IO.input(18)==True): #turn right  
                print("Condition 2")
                IO.output(32,True) #1A+
                IO.output(36,True) #1B-
                IO.output(38,True) #2A+
                IO.output(40,False) #2B-
            elif(IO.input(16)==True and IO.input(18)==False): #turn left
                print("Condition 3")
                IO.output(32,True) #1A+
                IO.output(36,False) #1B-
                IO.output(38,True) #2A+
                IO.output(40,True) #2B-
            else:  #stay still
                print("else condition")
                IO.output(32,True) #1A+
                IO.output(36,True) #1B-
                IO.output(38,True) #2A+
                IO.output(40,True) #2B-

#------------------------------------------------------------------------------#

def goStop():
    while 1:
     
            if(IO.input(16)==False and IO.input(18)==False): #both while move forward     
                print("Condition 1")
                IO.output(32,True) #1A+
                IO.output(36,False) #1B-
                IO.output(38,True) #2A+
                IO.output(40,False) #2B-
            elif(IO.input(16)==False and IO.input(18)==True): #turn right  
                print("Condition 2")
                IO.output(32,True) #1A+
                IO.output(36,True) #1B-
                IO.output(38,True) #2A+
                IO.output(40,False) #2B-
            elif(IO.input(16)==True and IO.input(18)==False): #turn left
                print("Condition 3")
                IO.output(32,True) #1A+
                IO.output(36,False) #1B-
                IO.output(38,True) #2A+
                IO.output(40,True) #2B-
            else:  #stay still
                print("else condition")
                IO.output(32,True) #1A+
                IO.output(36,True) #1B-
                IO.output(38,True) #2A+
                IO.output(40,True) #2B-

#------------------------------------------------------------------------------#

def goForward():
    while 1:
     
            if(IO.input(16)==False and IO.input(18)==False): #both while move forward     
                print("Condition 1")
                IO.output(32,True) #1A+
                IO.output(36,False) #1B-
                IO.output(38,True) #2A+
                IO.output(40,False) #2B-
            elif(IO.input(16)==False and IO.input(18)==True): #turn right  
                print("Condition 2")
                IO.output(32,True) #1A+
                IO.output(36,True) #1B-
                IO.output(38,True) #2A+
                IO.output(40,False) #2B-
            elif(IO.input(16)==True and IO.input(18)==False): #turn left
                print("Condition 3")
                IO.output(32,True) #1A+
                IO.output(36,False) #1B-
                IO.output(38,True) #2A+
                IO.output(40,True) #2B-
            else:  #stay still
                print("else condition")
                IO.output(32,True) #1A+
                IO.output(36,True) #1B-
                IO.output(38,True) #2A+
                IO.output(40,True) #2B-

#------------------------------------------------------------------------------#

       
fb();
updateMatrix();
numOfCustomers=input("How many are u there?"); 
#matr = [[1,1,0,1],[0,0,1,0],[2,0,0,2],[0,2,0,2]]
flag=0;       
j=0;
i=0;
table=0;
inde=1;
while j<4:
    i=0;
    mat=matr[j];
    while i<4:
        if(mat[i]*2>=int(numOfCustomers)):
            flag=1;
            #print("You can be seated at table number " + str(j+1) + "-"+ str(i+1));
            table=(j*4)+(i+1);
            print("Table Number: "+str(table))
            calPath(table);
            #voice("Table Number: "+str(table))
            break;
        i=i+1;
    if(flag==1):
        break;
    j=j+1;
if(table==0):
    voice("We are sorry for the inconvenience, We can't provide any more seats")
import bir
