import os
from gtts import gTTS
from pygame import mixer
from firebase import firebase
import tkinter as tk
import time
from tkinter import font  as tkfont
from PIL import ImageTk,Image

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (Camera, Details):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Camera")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Camera(tk.Frame):
##    app1=Tk()
    
    
   

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to the biryani point", font=controller.title_font)
        label.pack(side="top", fill="x", pady=100,padx=100)

##        button1 = tk.Button(self, text="RETAKE",
##                            command=lambda: controller.show_frame("PageTwo"))
        button2 = tk.Button(self, text="NEXT",
                            command=lambda: controller.show_frame("Details"))
        button2.pack()


class Details(tk.Frame):
    


    def __init__(self, parent, controller):
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
            except Exception as e:
                print(e)

        #------------------------------------------------------------------------------#
        



        def show_entry_fields():
            numOfCustomers=int(e1.get())
           
                

            fb();
            updateMatrix();
        #numOfCustomers=input("How many are u there?"); 
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





        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="How many are you there?", font=controller.title_font)
        e1 = tk.Entry(self)
        label.pack(side="top", fill="x", pady=2,padx=100)
        e1.pack(side="top",padx=20, pady=60)
        button = tk.Button(self, text="next",
                           command=show_entry_fields)
        button.pack()




if __name__ == "__main__":
       
        app = SampleApp()
        app.mainloop()





       
