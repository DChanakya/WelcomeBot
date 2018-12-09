import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.entry.pack()
        close_button = tk.Button(self, text="Submit", command=self.close)
        close_button.pack()
        self.string = ""

    def close(self):
        global result
        self.string = self.entry.get()
        self.destroy()

    def mainloop(self):
        tk.Tk.mainloop(self)
        return self.string

app = MyApp()
result = app.mainloop()
print ("you entered:", result)
