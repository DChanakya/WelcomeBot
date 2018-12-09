from tkinter import *
import os,time
from gtts import gTTS
from pygame import mixer
from firebase import firebase
firebase = firebase.FirebaseApplication('https://welcomebiryani-51293.firebaseio.com/', None)

matr=[];

#------------------------------------------------------------------------------#

def voice(string):
    tts = gTTS(text=string, lang='en')
    tts.save("sound.mp3")
    mixer.init()
    mixer.music.load("sound.mp3")
    mixer.music.play()
    
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



def show_entry_fields():
    fb();
    updateMatrix();
    numOfCustomers=e1.get(); 
    #matr = [[1,1,0,1],[0,0,1,0],[2,0,0,2],[0,2,0,2]]
    flag=0;       
    j=0;
    i=0;
    table=0;

    while j<4:
        i=0;
        mat=matr[j];
        while i<4:
            if(mat[i]*2>=int(numOfCustomers)):
                flag=1;
                #print("You can be seated at table number " + str(j+1) + "-"+ str(i+1));
                table=(j*4)+(i+1);
                voice("Table Number: "+str(table))
                break;
            i=i+1;
        if(flag==1):
            break;
        j=j+1;
    if(table==0):
        voice("We are sorry for the inconvenience, We can't provide any more seats")



master = Tk()
Label(master, text="How many are you there?").grid(row=0,padx=50,pady=60)

e1 = Entry(master)

e1.grid(row=0, column=1,padx=20)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4,padx=40)
Button(master, text='Next', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
