# 引入 Pillow module
from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk

root = Tk() 
root.title("Class1")
root.geometry("1000x300+150+150")

# 開啟圖片
img = Image.open("C:/Users/yoshi_pgnry07/Documents/Python_2023Spring/class1/logo_tree.png")
# 轉換為tk圖片物件
tk_img = ImageTk.PhotoImage(img)
# 設定程式icon
root.iconphoto(True,tk_img)

"""
# 建立 Label
label1 = Label(root, text="flat", relief="flat")
# 加入視窗
label1.pack()
label2 = Label(root, text="flat", relief="groove")
label2.pack()
label3 = Label(root, text="flat", relief="raised")
label3.pack()
label4 = Label(root, text="flat", relief="ridge")
label4.pack()
label5 = Label(root, text="flat", relief="solid")
label5.pack()
label6 = Label(root, text="flat", relief="sunken")
label6.pack()
label7 = Label(root, text="processing", relief="sunken", bg="white",fg="black",anchor=W,bd=2)
# 加入視窗
label7.pack(fill=X, side=BOTTOM)
"""
# """
# statusbar
# start button function
def start():
    val.set("processing...")
# stop buttom function
def stop():
    val.set("done")
# start buttom objext
Button1 = Button(root, text="Start", command=start)
# stop buttom object
Button2 = Button(root, text="Stop", command=stop)
Button1.pack()
Button2.pack()
# 建立val
val = StringVar()
val.set("Initialization...")
# 建立 Label
statusbar = Label(root, textvariable=val, relief="sunken", bg="white",fg="black",anchor=W,bd=2)
# 加入視窗
statusbar.pack(fill=X, side=BOTTOM)
# """
"""
table = ttk.Treeview(root, columns=["Product Name", "Unit Price", "Quantity", "Subtotal"])
# create columns title
table.heading("#0",text="Product Name")
table.heading("#1",text="Unit Price")
table.heading("#2",text="Quantity")
table.heading("#3",text="Subtotal")
# set column type
table.column("#0", width=250, anchor=CENTER)
table.column("#1", anchor=CENTER)
table.column("#2", anchor=CENTER)
table.column("#3", anchor=CENTER)
# 建立內容 從total行是用淺藍色底
table.tag_configure("totalcolor", background="#E7E2E2")
table.insert("",index="end",text="sofa",values=("2000","2","40000"))
# pack
table.pack()
"""

root.mainloop()