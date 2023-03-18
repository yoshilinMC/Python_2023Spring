from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
from tkscrolledframe import ScrolledFrame
from tkinter import ttk
from tkinter import filedialog

root = Tk() 
root.title("HW1")
root.geometry("400x300+150+150")

def Check():
    val4.set("廠牌 : "+ str(cbox.current()+1)+". "+cbox.get())
    if str(cbox.get()) == "BMW":
        val.set(BMW)
    elif str(cbox.get()) == "Mercedes":
        val.set(Mercedes)
    elif str(cbox.get()) == "Audi":
        val.set(Audi)
# List
val = StringVar()
BMW = ["1 Series (F40)","1 Series (F52)","2 Series Gran Coupé","2 Series","3 Series","4 Series","5 Series","6 Series","7 Series","8 Series","X1","X2","X3","X4","X5","X6","X7","Z4","2 Series Active Tourer","i3 (G28)","i4","i7","iX1","iX3","iX"]
Mercedes=["A-Class(Hatchbacks)","A-Class(Sedans)","C-Class","CLA","CLS","E-Class","EQE","EQS","S-Class","C-Class","CLA","E-Class","E-Class","EQA","EQB","EQC","G-Class","GLA","GLB","GLC","GLE","GLS","AMG GT","AMG GT 4-Door Coupé","AMG SL","AMG One","B-Class","Citan Van","Viano","EQV"]
Audi=["A1","A3","A4","A5","A6","A7","A8","e-tron GT","TT","R8","Q2","Q3","2019","Q4 e-tron","2021","Q5","Q5 e-tron","Q6","Q7","Q8","e-tron"]
# Label
val4 = StringVar()
val4.set("廠牌 :")
label = Label(root,text=" ",textvariable=val4)
label.grid(row=0,column=0,sticky=W)
# combobox
cbox = ttk.Combobox(root, values=["BMW", "Mercedes", "Audi"])
cbox.grid(row=1,column=0)
# Button
button = Button(root,text="OK",command=Check)
button.grid(row=2,column=0,sticky=W)
# ListBox
lbox = Listbox(root,selectmode="extended",listvariable=val)
lbox.grid(row=3,column=0,columnspan=3,sticky=W)

root.mainloop()