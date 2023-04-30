from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
from tkscrolledframe import ScrolledFrame
from tkinter import ttk
from tkinter import filedialog
from tkscrolledframe import ScrolledFrame
# import MimeText
from email.mime.text import MIMEText
# If we need pic for the email, we need MimeImage and use pathlib to read the pic
from email.mime.image import MIMEImage
from pathlib import Path
# import MimeMultipart
from email.mime.multipart import MIMEMultipart
# 設定 Gmail 的 SMTP server 寄送
import smtplib
from twilio.rest import Client
from pathlib import Path
import pygsheets
import pandas as pd
import requests
from tkvideo import tkvideo


root = Tk() 
root.title("Disney+")
root.geometry("600x800+150+0")

# # Create a ScrollFrame widget
# sframe1 = ScrolledFrame(root,width=300, height=300,bg="Pink")
# sframe1.grid()
# # Bind the arrow keys and scroll wheel
# sframe1.bind_arrow_keys(root)
# sframe1.bind_scroll_wheel(root)
# # create a frame within the ScrolledFrame
# inner_frame = sframe1.display_widget(Frame)

# Set google cloud user Know the identity
gc = pygsheets.authorize(service_file="class7/rational-world-383208-b189dfd24b52.json")
# Google sheets know the sheet
sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/1sMgqvFoYYULSSEHTlABPPYUmtFCZ-pd24G7b7aQYRCU/edit#gid=0")
ws = sht[0]

# # # Buy or Login
def Buy_Login():
    b_l = Toplevel()
    b_l.title("Buy or Login")
    b_l.geometry("150x150")
    # row0
    Buybtn = Button(b_l,text="Buy",command=Buy_1)
    Loginbtn = Button(b_l,text="Login",command=Login)
    Buybtn.grid(row=0,column=0,padx=5,pady=5,sticky=W+E+N+S)
    Loginbtn.grid(row=1,column=0,padx=5,pady=5,sticky=W+E+S+N)

# # buy
def Buy_1():
    Buy = Toplevel()
    Buy.title("Buy")
    Buy.geometry("300x300")
    # row0
    BuyLbl = Label(Buy, text="Email :")
    BuyLbl.grid(row=0,column=0)
    MailEntry = Entry(Buy)
    MailEntry.grid(row=1,column=0)
    BuyLbl2 = Label(Buy, text="信用卡號 :")
    BuyLbl2.grid(row=2,column=0)
    NumEntry = Entry(Buy)
    NumEntry.grid(row=3,column=0)
    pslbl = Label(Buy,text="密碼 :")
    pslbl.grid(row=4,column=0)
    psentry = Entry(Buy)
    psentry.grid(row=5,column=0)
    Enterbtn = Button(Buy, text="Buy",command=lambda:Buy_22(Buy,MailEntry,NumEntry,psentry))
    Enterbtn.grid(row=6,column=0)
    Buy.mainloop()

####### 發EMAIL
def Buy_22(screem,maile,creditCarde,passworde):
    def Check():
        if str(CheckEntry.get()) == "abcde":
            OKLbl = Label(Buy_2,text="Success")
            OKLbl.grid(row=2,column=0,sticky=W+S+N+E)
            Buy_2.destroy()
            screem.destroy()
        else:
            OKLbl = Label(Buy_2,text="Wrong")
            OKLbl.grid(row=2,column=0,sticky=W+S+N+E)
    Buy_2 = Toplevel()
    Buy_2.title("Info")
    Buy_2.geometry("150x150")
    CheckEntry = Entry(Buy_2)
    CheckEntry.grid(row=0,column=0)
    Checkbtn = Button(Buy_2,text="Check",command=Check)
    Checkbtn.grid(row=1,column=0)
    # # #
    Email = maile.get()
    creditCard = creditCarde.get()
    password = passworde.get()
    print("Email:"+str(Email)+"\nCredit Card:"+str(creditCard)+"\nPassword:"+str(password))
    df = pd.DataFrame(ws.get_all_records())
    df.loc[len(df.index)] = [str(Email), str(creditCard), str(password)]
    print(df)
    ws.set_dataframe(df, 'A1') #從欄位 A1 開始
    result = Label(root, text="Registration Success...",fg="red")
    result.grid(row=9,column=0, columnspan=3, sticky=W+S)
    Buy_2.mainloop()

# # Login
def Login():
    def loginfun(email,password):
        df = pd.DataFrame(ws.get_all_records())
        df_result = df[df["Email"]==email]
        if (len(df_result)) >= 1:
            print(type(df_result["password"][0]),type(password))
            # 帳號對的時候
            if ((str(df_result["password"][0]))==password):
                # 帳號密碼都對的狀況
                print(df_result["password"])
                result = Label(Login, text="Correct, You may start your movie",fg="red")
                result.grid(row=5,column=0, columnspan=3, sticky=W+S)
            else:
                # 帳號對密碼錯
                result = Label(Login, text="Wrong password",fg="red")
                result.grid(row=5,column=0, columnspan=3, sticky=W+S)
        else:
            # 找不到帳號
            result = Label(Login, text="Email not found",fg="red")
            result.grid(row=5,column=0, columnspan=3, sticky=W+S)
    Login = Toplevel()
    Login.title("Login")
    Login.geometry("300x300")
    Emaillbl = Label(Login,text="Email")
    Emaillbl.grid(row=0,column=0)
    EmailEty = Entry(Login)
    EmailEty.grid(row=1,column=0)
    PWlbl = Label(Login,text="Password")
    PWlbl.grid(row=2,column=0)
    PWEty = Entry(Login)
    PWEty.grid(row=3,column=0)
    Enterbtn = Button(Login,text="Login", command=lambda:loginfun(EmailEty.get(),PWEty.get()))
    Enterbtn.grid(row=4,column=0)

# # video
def video(mov):
    playVideo = Toplevel()
    playVideo.title("video")
    playVideo.geometry("1300x750+0+0")
    videolabel = Label(playVideo)
    videolabel.grid(row=0,column=0)
    play = tkvideo(mov,videolabel,loop=1,size=(1280,720))
    play.play()
    exitbtn = Button(playVideo,text="Exit",command=playVideo.destroy)
    exitbtn.grid(row=1,column=0,sticky=E+N+S)
    playVideo.mainloop()

# # root 
# row0
DisneyImage = Image.open("Project/Pic/Disney.jpg")
DisneyImage = DisneyImage.resize((480,300))
DisneyImage = ImageTk.PhotoImage(DisneyImage)
Disneybtn = Button(root, image=DisneyImage,command=Buy_Login,width=480,height=200)
Disneybtn.grid(row=0,column=0,columnspan=8,padx=0,sticky=N+S)

# row1
BannerImage = Image.open("Project/Pic/曼達.jpg")
BannerImage = BannerImage.resize((480,200))
BannerImage = ImageTk.PhotoImage(BannerImage)
BannerLabel = Label(root, image=BannerImage)
BannerLabel.grid(row=1,column=0,columnspan=8,padx=5,sticky=W+N+S+E) 

# row2
DisneyImg = Image.open("Project/Pic/DisneyImg.jpg")
DisneyImg = DisneyImg.resize((180,50))
DisneyImg = ImageTk.PhotoImage(DisneyImg)
PIXARImg = Image.open("Project/Pic/Pixar.jpg")
PIXARImg = PIXARImg.resize((180,50))
PIXARImg = ImageTk.PhotoImage(PIXARImg)
MarvelImg = Image.open("Project/Pic/Marvel.jpg")
MarvelImg = MarvelImg.resize((180,50))
MarvelImg = ImageTk.PhotoImage(MarvelImg)
Disneylbl = Button(root, image=DisneyImg)
Disneylbl.grid(row=2,column=0,columnspan=2,padx=5,sticky=W)
PIXARlbl = Button(root, image=PIXARImg)
PIXARlbl.grid(row=2,column=2,columnspan=2,padx=5,sticky=W+E)
Marvellbl = Button(root, image=MarvelImg)
Marvellbl.grid(row=2,column=4,columnspan=2,padx=5,sticky=E)
# row3
SWImg = Image.open("Project/Pic/StarWars.jpg")
SWImg = SWImg.resize((180,50))
SWImg = ImageTk.PhotoImage(SWImg)
NGImg = Image.open("Project/Pic/National.jpg")
NGImg = NGImg.resize((180,50))
NGImg = ImageTk.PhotoImage(NGImg)
StarImg = Image.open("Project/Pic/Star.jpg")
StarImg = StarImg.resize((180,50))
StarImg = ImageTk.PhotoImage(StarImg)
SWlbl = Button(root, image=SWImg)
SWlbl.grid(row=3,column=0,columnspan=2,padx=5,sticky=W)
NGlbl = Button(root, image=NGImg)
NGlbl.grid(row=3,column=2,columnspan=2,padx=5,sticky=W+E)
Starlbl = Button(root, image=StarImg)
Starlbl.grid(row=3,column=4,columnspan=2,padx=5,sticky=E)

# row4
FamousMovLbl = Label(root,text="熱門電影 :")
FamousMovLbl.grid(row=4,column=0,sticky=W+S+N)

# row5 
DrImg = Image.open("Project/Pic/Strange.jpg")
DrImg = DrImg.resize((150,200))
DrImg = ImageTk.PhotoImage(DrImg)
SCImg = Image.open("Project/Pic/ShanChi.jpg")
SCImg = SCImg.resize((150,200))
SCImg = ImageTk.PhotoImage(SCImg)
LeoImg = Image.open("Project/Pic/黑豹2.jpg")
LeoImg = LeoImg.resize((150,200))
LeoImg = ImageTk.PhotoImage(LeoImg)

Drbtn = Button(root, image=DrImg,command=lambda:video("Project/Pic/Dr.StrangeMov.mp4"))
Drbtn.grid(row=5,column=0,padx=5,sticky=W+S+N)
SCbtn = Button(root, image=SCImg,command=lambda:video("Project/Pic/Leo2Mov.mp4"))
SCbtn.grid(row=5,column=2,padx=5,sticky=W+S+N)
Leobtn = Button(root, image=LeoImg,command=lambda:video("Project/Pic/ShanChiMov.mp4"))
Leobtn.grid(row=5,column=4,padx=5,sticky=W+S+N)

root.mainloop()