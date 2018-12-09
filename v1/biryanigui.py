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
        def show_entry_fields():
           print("First Name: %s\n" % (e1.get()))
           if(int(e1.get())>4):
               print("Sorry for the inconvinience we cannot you tables more than 4")
               
           else:
                print("Come I will take you to your table")
                

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
