# 引入 Pillow module
from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
from tkscrolledframe import ScrolledFrame

root = Tk() 
root.title("Class2")
root.geometry("300x200+150+150")

"""
val = StringVar()
def choose():
    Label_Choose["textvariable"] = val
PlaceLabel = Label(root,text="你要去?")
PlaceLabel.grid(column=0,row=0)
rdbtn1 = Radiobutton(root,text="東京",command=choose,variable=val, value="東京")
rdbtn1.grid(column=0,row=1)
rdbtn1 = Radiobutton(root,text="德國",command=choose,variable=val, value="德國")
rdbtn1.grid(column=1,row=1)
rdbtn1.select()
rdbtn1 = Radiobutton(root,text="紐約",command=choose,variable=val, value="紐約")
rdbtn1.grid(column=2,row=1)
Label_Choose = Label(root, textvariable=val)
Label_Choose.grid(column=0,row=2)
"""
"""
val = StringVar()
val2 = StringVar()
val3 = StringVar()
def Check():
    text = (val.get())+" "+(val2.get())+" "+(val3.get())
    Label_Choose["text"]=text
PlaceLabel = Label(root,text="你要去?")
PlaceLabel.grid(column=0,row=0,sticky=W)
chbtn1 = Checkbutton(root,text="直飛",command=Check,variable=val, onvalue="直飛",offvalue=" ")
chbtn1.grid(column=0,row=1,sticky=W)
chbtn2 = Checkbutton(root,text="轉機1次",command=Check,variable=val2, onvalue="轉機1次",offvalue=" ")
chbtn2.grid(column=1,row=1,sticky=W)
chbtn2.select()
chbtn3 = Checkbutton(root,text="轉機2次",command=Check,variable=val3, onvalue="轉機2次",offvalue=" ")
chbtn3.grid(column=2,row=1,sticky=W)
Label_Choose = Label(root, text="",anchor=W,relief="sunken",fg="Black",bg="White")
Label_Choose.grid(column=0,row=2,sticky=W+E+S+N)
"""

# Create a ScrollFrame widget
sframe1 = ScrolledFrame(root,width=300, height=300)
sframe1.pack()
# Bind the arrow keys and scroll wheel
sframe1.bind_arrow_keys(root)
sframe1.bind_scroll_wheel(root)
# create a frame within the ScrolledFrame
inner_frame = sframe1.display_widget(Frame)
btn1 = Button(inner_frame,text="1",height=50,bg="black")
btn2 = Button(inner_frame,text="2",height=50,bg="black")
btn3 = Button(inner_frame,text="3",height=50,bg="black")
btn4 = Button(inner_frame,text="4",height=50,bg="black")
btn5 = Button(inner_frame,text="5",height=50,bg="black")
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()

root.mainloop()