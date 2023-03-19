from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
from tkscrolledframe import ScrolledFrame
from tkinter import ttk
from tkinter import filedialog

root = Tk() 
root.title("HW1")
root.geometry("400x300+150+150")

"""
# def
def choose(e):
    val.set("年齡 : " + str(year_scale.get()))
# val
val = StringVar()
val.set("年齡 : 0")
# Scale
year_scale = Scale(root, from_=0, to=100, orient=HORIZONTAL,command=choose)
year_scale.grid(row=1, column=0, columnspan=3)
# Label
label = Label(root, textvariable=val)
label.grid(row=2,column=0,sticky=W)
"""
"""
def choose(): 
    val.set("身高 : " + str(box.get()))
# val
val = StringVar()
val.set("身高 : 100")
# Scale
box = Spinbox(root, from_=100, to=250,command=choose)
box.grid(row=1, column=0, columnspan=3)
# Label
label = Label(root, textvariable=val)
label.grid(row=2,column=0,sticky=W)
"""
# val
val = StringVar()
val2 = StringVar()
val3 = StringVar()
Colorval = StringVar()
val.set("R : 0")
val2.set("G : 0")
val3.set("B : 0")
# def
def choose(e): 
    val.set("R : " + str(year_scale1.get()))
    val2.set("G : " + str(year_scale2.get()))
    val3.set("B : " + str(year_scale3.get()))
    ColorLabel["bg"] = "#" + "(0:2x)(1:2x)(2:2x)".format(year_scale1.get(),year_scale2.get(),year_scale3.get())
# Choose 
label = Label(root,text="choose ur color(R,G,B)")
label.grid(row=0,column=0)
# Label
label1 = Label(root, textvariable=val)
label1.grid(row=1,column=0,sticky=W)
label2 = Label(root, textvariable=val2)
label2.grid(row=3,column=0,sticky=W)
label3 = Label(root, textvariable=val3)
label3.grid(row=5,column=0,sticky=W)
# Scale
year_scale1 = Scale(root, from_=0, to=256, orient=HORIZONTAL,command=choose)
year_scale1.grid(row=2, column=0, columnspan=3,sticky=W)
year_scale2 = Scale(root, from_=0, to=256, orient=HORIZONTAL,command=choose)
year_scale2.grid(row=4, column=0, columnspan=3,sticky=W)
year_scale3 = Scale(root, from_=0, to=256, orient=HORIZONTAL,command=choose)
year_scale3.grid(row=6, column=0, columnspan=3,sticky=W)
# Color
ColorLabel = Label(root,textvariable=Colorval,relief="sunken",width=30)
ColorLabel.grid(row=7,column=0)

root.mainloop()