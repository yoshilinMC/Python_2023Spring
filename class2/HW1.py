# 引入 Pillow module
from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
from tkscrolledframe import ScrolledFrame

root = Tk() 
root.title("Class2")
root.geometry("300x100+150+150")

# Create a ScrollFrame widget
sframe1 = ScrolledFrame(root,width=300, height=300)
sframe1.pack()
# Bind the arrow keys and scroll wheel
sframe1.bind_arrow_keys(root)
sframe1.bind_scroll_wheel(root)
# create a frame within the ScrolledFrame
inner_frame = sframe1.display_widget(Frame)

val = StringVar()
val2 = StringVar()
val3 = StringVar()
val4 = StringVar()
val5 = StringVar()
val6 = StringVar()
def Check():
    text = (val.get())+" "+(val2.get())+" "+(val3.get())+" "+(val4.get())+" "+(val5.get())+" "+(val6.get())
    Label_Choose["text"]=text
PlaceLabel = Label(inner_frame,text="你的主餐?")
PlaceLabel.grid(column=0,row=0,sticky=W)
chbtn1 = Checkbutton(inner_frame,text="和牛",command=Check,variable=val, onvalue="和牛",offvalue=" ")
chbtn1.grid(column=0,row=1,sticky=W)
chbtn2 = Checkbutton(inner_frame,text="伊比利豬",command=Check,variable=val2, onvalue="伊比利豬",offvalue=" ")
chbtn2.grid(column=1,row=1,sticky=W)
chbtn3 = Checkbutton(inner_frame,text="海鮮",command=Check,variable=val3, onvalue="海鮮",offvalue=" ")
chbtn3.grid(column=2,row=1,sticky=W)
PlaceLabel2 = Label(inner_frame,text="你的飲料?")
PlaceLabel2.grid(column=0,row=3,sticky=W)
chbtn3 = Checkbutton(inner_frame,text="咖啡",command=Check,variable=val4, onvalue="咖啡",offvalue=" ")
chbtn3.grid(column=0,row=4,sticky=W)
chbtn4 = Checkbutton(inner_frame,text="紅茶",command=Check,variable=val5, onvalue="紅茶",offvalue=" ")
chbtn4.grid(column=1,row=4,sticky=W)
chbtn3 = Checkbutton(inner_frame,text="奶茶",command=Check,variable=val6, onvalue="奶茶",offvalue=" ")
chbtn3.grid(column=2,row=4,sticky=W)
Label_Choose = Label(inner_frame, text="",anchor=W,relief="sunken",fg="Black",bg="White")
Label_Choose.grid(column=0,row=5,sticky=W+E+S+N,columnspan=5)

root.mainloop()