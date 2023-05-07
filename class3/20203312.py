# 引入 Pillow module, ttk 加強, filedialog
from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
from tkscrolledframe import ScrolledFrame
from tkinter import ttk
from tkinter import filedialog

root = Tk() 
root.title("Class3")
root.geometry("400x300+150+150")

# """
# Create a ScrollFrame widget
sframe1 = ScrolledFrame(root,width=300, height=300,bg="Pink")
sframe1.pack()
# Bind the arrow keys and scroll wheel
sframe1.bind_arrow_keys(root)
sframe1.bind_scroll_wheel(root)
# create a frame within the ScrolledFrame
inner_frame = sframe1.display_widget(Frame)
btn1 = Button(inner_frame,text="1",height=50 )
btn2 = Button(inner_frame,text="2",height=50 )
btn3 = Button(inner_frame,text="3",height=50 )
btn4 = Button(inner_frame,text="4",height=50 )
btn5 = Button(inner_frame,text="5",height=50 )
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
# """
"""
def Check():
    val.set("廠牌 : "+ str(box.current()+1)+". "+box.get())
val = StringVar()
val.set("廠牌 :")
# Label
label = Label(root,text=" ",textvariable=val)
label.grid(row=0,column=0,sticky=W)
# combobox
box = ttk.Combobox(root, values=["MBW", "Benz", "Audi"])
box.grid(row=1,column=0)
# Button
button = Button(root,text="OK",command=Check)
button.grid(row=2,column=0,sticky=W)
"""
"""
# Listbox
listbox = Listbox(root,selectmode=EXTENDED)
listbox.insert(1,"A1")
listbox.insert(2,"A2")
listbox.insert(3,"A3")
listbox.pack()
"""
"""
def choose():
    label["text"] = box.get(box.curselection())
# List BMW
val = StringVar()
BMW = ["1 Series (F40)","1 Series (F52)","2 Series Gran Coupé","2 Series","3 Series","4 Series","5 Series","6 Series","7 Series","8 Series","X1","X2","X3","X4","X5","X6","X7","Z4","2 Series Active Tourer","i3 (G28)","i4","i7","iX1","iX3","iX"]
# 儲存
val.set(BMW)
# ListBox
box = Listbox(root,selectmode="extended", listvariable=val)
box.grid(row=0,column=0,columnspan=3,sticky=W)
# Button
btn = Button(root,text="choose",command=choose)
btn.grid(row=1,column=0,sticky=W)
# Label
label = Label(root,text="", fg="black", bg="white",anchor=W, relief="sunken",bd=2)
label.grid(row=3,column=0,columnspan=3,sticky=W+E+S)
"""
"""
def choose():
    filePath = filedialog.askopenfilename(title="選取照片",initialdir="C:/Users/yoshi_pgnry07/Documents",multiple = False)
    image = Image.open(filePath)
    re_image = image.resize((150,100))
    global tk_image
    tk_image = ImageTk.PhotoImage(image)
    label["image"]=tk_image
btn = Button(text="Choose",command=choose)
btn.pack()
label = Label(root)
label.pack()
"""

root.mainloop()