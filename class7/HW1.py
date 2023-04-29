from twilio.rest import Client
from pathlib import Path
import pygsheets
from tkinter import *
import tkinter.ttk as ttk
import pandas as pd

root = Tk() 
root.title("HW1")
root.geometry("400x400+150+150")

# Set google cloud user Know the identity
gc = pygsheets.authorize(service_file="class7/rational-world-383208-b189dfd24b52.json")
# Google sheets know the sheet
sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/1sMgqvFoYYULSSEHTlABPPYUmtFCZ-pd24G7b7aQYRCU/edit#gid=0")

val = Variable()
val2 = Variable()
val3 = Variable()
val4 = Variable()
val5 = Variable()

def Sign():
    # ws.update_value("A2",val)
    # ws.update_value("B2",val2)
    # ws.update_value("C2",val3)
    # ws.update_value("D2",val4)
    name = Namebx.get()
    mail = Emailbx.get()
    ps = PSbx.get()
    pn = PNbx.get()

    print("Name: "+str(name)+"\nEmail :"+str(mail)+"\nPassword"+str(ps)+"\nPhone Number"+str(pn))
    df = pd.DataFrame(ws.get_all_records())
    df.loc[len(df.index)] = [str(name), str(mail), str(ps), str(pn)]
    print(df)
    ws.set_dataframe(df, "A1")

    # 1
    result = Label(root, text="Access", fg="red")
    result.grid(row=9,column=0,columnspan=3,sticky=W+S)

ws = sht[0]
ws.update_value("A1","Name")
ws.update_value("B1","Email")
ws.update_value("C1","Password")
ws.update_value("D1","Phone Number")

Namelbl = Label(text="Name:")
Namelbl.grid(column=0,row=0,sticky=W)
Emaillbl = Label(text="Email:")
Emaillbl.grid(column=0,row=2,sticky=W)
PWlbl = Label(text="Password:")
PWlbl.grid(column=0,row=4,sticky=W)
PNlbl = Label(text="Phone Number:")
PNlbl.grid(column=0,row=6,sticky=W)
Namebx = Entry(textvariable=val)
Namebx.grid(column=0,row=1,sticky=W)
Emailbx = Entry(textvariable=val2)
Emailbx.grid(column=0,row=3,sticky=W)
PSbx = Entry(textvariable=val3)
PSbx.grid(column=0,row=5,sticky=W)
PNbx = Entry(textvariable=val4)
PNbx.grid(column=0,row=7,sticky=W)
Loginbtn = Button(text="Sign up",command=Sign)
Loginbtn.grid(column=0,row=8,sticky=W+E+S+N)

root.mainloop()