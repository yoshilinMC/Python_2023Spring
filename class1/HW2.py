# 引入 Pillow module
from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk

root = Tk() 
root.title("HW2")
root.geometry("1000x300+150+150")

def CreateNewWindow():
    # 建立新視窗 showdetail
    NewWindows = Toplevel(root)
    NewWindows = Tk() 
    NewWindows.title("HW2")
    NewWindows.geometry("1000x300+150+150")
    # create table
    treeview_name = ttk.Treeview(NewWindows, columns=["Product Name", "Unit Price", "Quantity", "Subtotal"])
    # create columns title
    treeview_name.heading("#0",text="Product Name")
    treeview_name.heading("#1",text="Unit Price")
    treeview_name.heading("#2",text="Quantity")
    treeview_name.heading("#3",text="Subtotal")
    # set column type
    treeview_name.column("#0", width=250, anchor=CENTER)
    treeview_name.column("#1", anchor=CENTER)
    treeview_name.column("#2", anchor=CENTER)
    treeview_name.column("#3", anchor=CENTER)
    # 建立內容 從total行是用淺藍色底
    treeview_name.tag_configure("totalcolor", background="#E7E2E2")
    treeview_name.insert("",index="end",text="sofa",values=("2000","2","40000"))
    # pack
    treeview_name.pack()

ShowDetailWindowBtn = Button(root, text="Click to Create New Windows!", command=CreateNewWindow)
ShowDetailWindowBtn.pack()

root.mainloop()