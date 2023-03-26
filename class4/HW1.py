# 引入 Pillow module, ttk 加強, filedialog
from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
from tkscrolledframe import ScrolledFrame
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title("HW1")
root.geometry("400x300+150+150")

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
    r = int(year_scale1.get())
    g = int(year_scale2.get())
    b = int(year_scale3.get())
    hex = "#{:02x}{:02x}{:02x}".format(r,g,b)
    Colorval.set(hex)
    ColorLabel["bg"] = hex
    val.set(r)
    val2.set(g)
    val3.set(b)
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
year_scale1 = Scale(root, from_=0, to=255, orient=HORIZONTAL,command=choose,length=300)
year_scale1.grid(row=2, column=0, columnspan=3,sticky=W)
year_scale2 = Scale(root, from_=0, to=255, orient=HORIZONTAL,command=choose,length=300)
year_scale2.grid(row=4, column=0, columnspan=3,sticky=W)
year_scale3 = Scale(root, from_=0, to=255, orient=HORIZONTAL,command=choose,length=300)
year_scale3.grid(row=6, column=0, columnspan=3,sticky=W)
# Color
ColorLabel = Label(root,textvariable=Colorval,relief="sunken",width=30,bg="white")
ColorLabel.grid(row=7,column=0)

root.mainloop()