# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 00:21:26 2015

@author: Timothy
"""

from Tkinter import*

#Create window
root = Tk()

#Modify root window
root.title("User Interface")
root.geometry("400x400")

app = Frame(root)
app.grid()
label = Label(app, text = "This is a label")
label.grid()

button1 = Button(app, text = "Start Simulation")
button1.grid()

button2 = Button(app)
button2.grid()
button2.configure(text = "Stop Simulation")

button3 = Button(app)
button3.grid()
button3["text"] = "Programmable title"

#Start event loop
root.mainloop()