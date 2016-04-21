# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 00:30:56 2015

@author: Timothy
"""

from Tkinter import*

class Application(Frame):
    
    def __init__(self, master):
        """Initialize the Frame"""
        Frame.__init__(self, master)
        self.grid()
        self.button1_clicks = 0
        self.create_widgets()
                
        
    def create_widgets(self):
        self.button1 = Button(self)
        self.button1["text"] = "Total clicks: 0"        
        self.button1["command"] = self.update_count     #bind the event handler       
        self.button1.grid()

    def update_count(self):
        self.button1_clicks += 1
        self.button1["text"] = "Total clicks: " + str(self.button1_clicks)



#        self.button2 = Button(self)
#        self.button2.grid()
#        self.button2.configure(text = "second button")
#
#        self.button3 = Button(self)
#        self.button3.grid()
#        self.button3["text"] = "third button"        
        
root = Tk()
root.title("OOP GUI")
root.geometry("400x400")

app = Application(root)
root.mainloop()