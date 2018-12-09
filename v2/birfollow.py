import tkinter as tk
import time
from tkinter import font  as tkfont
from PIL import ImageTk,Image
import cv2
import qrcode
##400*840
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='systemfixed', size=24, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(1,minsize=84)
        container.grid_columnconfigure(0,minsize=40, weight=1)
        self.frames = {}
        for F in (Camera, Details):
            page_name = F.__name__
            frame = F(parent=container,controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=3, sticky="nsew")

        self.show_frame("Camera")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Camera(tk.Frame):
##    app1=Tk()
    def __init__(self, parent, controller):
         def show_entry_fields():
             cap = cv2.VideoCapture(0) 
             

             while(True):
                font = cv2.FONT_HERSHEY_SIMPLEX
                ret,frame = cap.read() 
                id="saran"
                img=frame
                cv2.putText(img,'Click Y to for your image',(20,50), font, 1.3,(0,255,0),2,cv2.LINE_AA)
                cv2.imshow('img1',img) 
                if (cv2.waitKey(1) & 0xFF == ord('y')): #save on pressing 'y' 
                    cv2.imw