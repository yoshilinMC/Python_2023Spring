# 引入 Pillow module
from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk

root = Tk() 
root.title("HW1")
root.geometry("1000x300+150+150")

# statusbar
# start button function
def start():
    val.set("運行中...")
# stop buttom function
def stop():
    val.set("已停止...")
# start buttom objext
Button1 = Button(root, text="Start", command=start)
# stop buttom object
Button2 = Button(root, text="Stop", command=stop)
Button1.pack()
Button2.pack()
# 建立val
val = StringVar()
val.set("運行中...")
# 建立 Label
statusbar = Label(root, textvariable=val, relief="sunken", bg="white",fg="black",anchor=W,bd=2)
# 加入視窗
statusbar.pack(fill=X, side=BOTTOM)

root.mainloop()