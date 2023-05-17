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
from random import *
from tkinter import messagebox

root = Tk() 
root.title("Disney+")
root.geometry("600x800+150+0")

# Create a ScrollFrame widget
sframe1 = ScrolledFrame(root,width=600,height=800,bg="white")
sframe1.grid()
# Bind the arrow keys and scroll wheel
sframe1.bind_arrow_keys(root)
sframe1.bind_scroll_wheel(root)
# create a frame within the ScrolledFrame
inner_frame = sframe1.display_widget(Frame)

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
    Enterbtn = Button(Buy, text="Buy",command=lambda:Buy_22(Buy,MailEntry.get(),NumEntry.get(),psentry.get()))
    Enterbtn.grid(row=6,column=0)
    Buy.mainloop()

def Buy_22(screen,maile,creditCarde,passworde):
    password = randint(1000,9999)
    # MimeText
    text = MIMEText("This is the password of your Disney+ Acount : "+str(password))
    # Use bytes for reading the pic
    image = MIMEImage(Path("Project/Pic/Disney.jpg").read_bytes())
    # MimeMultiPart
    content = MIMEMultipart()
    # Title
    content["subject"] = "Disney+ Create New Acount Password"
    # 收件
    content["from"] = "yoshilin2.0@gmail.com"
    # 寄件
    content["to"] = str(maile)
    print(maile)
    # content
    content.attach(text)
    # Img content
    content.attach(image)
    # smtplib
    smtp = smtplib.SMTP(host="smtp.gmail.com", port="587")
    # use with auto freed the resource
    with open("Project/password.txt", "r") as f:
        mailToken = f.read()
    with smtp:
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("yoshilin2.0@gmail.com", mailToken)
            smtp.send_message(content)
            messagebox.showinfo('my messagebox', 'The Email is Sended Completely')
            smtp.quit()
        except Exception as e:
            print("Error Message: ",e)
    Buy_2 = Toplevel()
    Buy_2.title("Info")
    Buy_2.geometry("150x150")
    CheckLbl = Label(Buy_2,text="Enter The Password")
    CheckLbl.grid(row=0,column=0)
    CheckEntry = Entry(Buy_2)
    CheckEntry.grid(row=1,column=0)
    Checkbtn = Button(Buy_2,text="Check",command=lambda:Check(password,CheckEntry.get(),Buy_2,screen,maile,creditCarde,passworde))
    Checkbtn.grid(row=2,column=0)
    Buy_2.mainloop()

# # Send Email
def Check(enterPassword,realPassword,screen_2,screen,Email,CreditCard,Password):
    print("Email:"+str(Email)+"\nCredit Card:"+str(CreditCard)+"\nPassword:"+str(Password))
    df = pd.DataFrame(ws.get_all_records())
    df.loc[len(df.index)] = [str(Email), str(CreditCard), str(Password)]
    print(df)
    ws.set_dataframe(df, 'A1') #從欄位 A1 開始
    result = Label(inner_frame, text="Registration Success...",fg="red")
    result.grid(row=9,column=0, columnspan=3, sticky=W+S)
    if str(enterPassword) == str(realPassword):
        OKLbl = Label(screen_2,text="Success")
        OKLbl.grid(row=2,column=0,sticky=W+S+N+E) 
        screen_2.destroy()
        screen.destroy()
    else:
        OKLbl = Label(screen_2,text="Wrong")
        OKLbl.grid(row=2,column=0,sticky=W+S+N+E)

# # Login
def Login():
    def loginfun(email,password):
        df = pd.DataFrame(ws.get_all_records())
        df_result = df[df["Email"]==email]
        # print(type(df_result["password"][0]),type(password))
        if (len(df_result)) >= 1:
            # 帳號對的時候
            print(df_result["password"])
            if ((str(list(df_result["password"])[0]))==password):
                # 帳號密碼都對的狀況
                messagebox.showinfo('my messagebox', 'Correct, You may start your movie')
                Login.destroy()
            else:
                # 帳號對密碼錯
                messagebox.showwarning('my messagebox', 'Wrong Password')
        else:
            # 找不到帳號
            messagebox.showwarning('my messagebox', 'Email Not Found')
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

# # Disney
def Disney():
    root_v2 = Toplevel() 
    root_v2.title("Disney")
    root_v2.geometry("500x700+150+0")
    # row0
    NiceMovLbl = Label(root_v2,text="原創 :")
    NiceMovLbl.grid(row=0,column=0,sticky=W+S+N)
    # row1
    FirstImg = Image.open("Project/Pic/Dance.jpg")
    FirstImg = FirstImg.resize((150,200))
    FirstImg = ImageTk.PhotoImage(FirstImg)
    SecondtImg = Image.open("Project/Pic/disney111.jpg")
    SecondtImg = SecondtImg.resize((150,200))
    SecondtImg = ImageTk.PhotoImage(SecondtImg)
    ThirdtImg = Image.open("Project/Pic/Peter.jpg")
    ThirdtImg = ThirdtImg.resize((150,200))
    ThirdtImg = ImageTk.PhotoImage(ThirdtImg)
    # # #
    Firstbtn = Button(root_v2, image=FirstImg,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn.grid(row=1,column=0,padx=5,sticky=W+S+N)
    Secondbtn = Button(root_v2, image=SecondtImg,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn.grid(row=1,column=2,padx=5,sticky=W+S+N)
    Thirdbtn = Button(root_v2, image=ThirdtImg,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    Thirdbtn.grid(row=1,column=4,padx=5,sticky=W+S+N)
    # row2
    NewMovLbl = Label(root_v2,text="迪士尼動畫工作室 :")
    NewMovLbl.grid(row=2,column=0,sticky=W+S+N)
    # row3
    FirstImg_2 = Image.open("Project/Pic/Magic.jpg")
    FirstImg_2 = FirstImg_2.resize((150,200))
    FirstImg_2 = ImageTk.PhotoImage(FirstImg_2)
    SecondtImg_2 = Image.open("Project/Pic/Moana.jpg")
    SecondtImg_2 = SecondtImg_2.resize((150,200))
    SecondtImg_2 = ImageTk.PhotoImage(SecondtImg_2)
    ThirdtImg_2 = Image.open("Project/Pic/Dumbo.jpg")
    ThirdtImg_2 = ThirdtImg_2.resize((150,200))
    ThirdtImg_2 = ImageTk.PhotoImage(ThirdtImg_2)
    # # #
    Firstbtn_2 = Button(root_v2, image=FirstImg_2,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn_2.grid(row=3,column=0,padx=5,sticky=W+S+N)
    Secondbtn_2 = Button(root_v2, image=SecondtImg_2,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn_2.grid(row=3,column=2,padx=5,sticky=W+S+N)
    Thirdbtn_2 = Button(root_v2, image=ThirdtImg_2,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    Thirdbtn_2.grid(row=3,column=4,padx=5,sticky=W+S+N)
    # row4
    NewMovLbl_1 = Label(root_v2,text="冰雪奇緣 :")
    NewMovLbl_1.grid(row=4,column=0,sticky=W+S+N)
    # row5
    FirstImg_3 = Image.open("Project/Pic/Frozen.jpg")
    FirstImg_3 = FirstImg_3.resize((150,200))
    FirstImg_3 = ImageTk.PhotoImage(FirstImg_3)
    SecondtImg_3 = Image.open("Project/Pic/Frozen2.jpg")
    SecondtImg_3 = SecondtImg_3.resize((150,200))
    SecondtImg_3 = ImageTk.PhotoImage(SecondtImg_3)
    ThirdtImg_3 = Image.open("Project/Pic/Snow.jpg")
    ThirdtImg_3 = ThirdtImg_3.resize((150,200))
    ThirdtImg_3 = ImageTk.PhotoImage(ThirdtImg_3)
    # # #
    Firstbtn_3 = Button(root_v2, image=FirstImg_3,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn_3.grid(row=5,column=0,padx=5,sticky=W+S+N)
    Secondbtn_3 = Button(root_v2, image=SecondtImg_3,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn_3.grid(row=5,column=2,padx=5,sticky=W+S+N)
    Thirdbtn_3 = Button(root_v2, image=ThirdtImg_3,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    Thirdbtn_3.grid(row=5,column=4,padx=5,sticky=W+S+N)

    root_v2.mainloop()

# # Pixar
def Pixar():
    root_v2 = Toplevel() 
    root_v2.title("Pixar")
    root_v2.geometry("500x700+150+0")
    # row0
    NiceMovLbl = Label(root_v2,text="精選 :")
    NiceMovLbl.grid(row=0,column=0,sticky=W+S+N)
    # row1
    FirstImg = Image.open("Project/Pic/toystory.jpg")
    FirstImg = FirstImg.resize((150,200))
    FirstImg = ImageTk.PhotoImage(FirstImg)
    SecondtImg = Image.open("Project/Pic/insideOut.jpg")
    SecondtImg = SecondtImg.resize((150,200))
    SecondtImg = ImageTk.PhotoImage(SecondtImg)
    ThirdtImg = Image.open("Project/Pic/coco.jpg")
    ThirdtImg = ThirdtImg.resize((150,200))
    ThirdtImg = ImageTk.PhotoImage(ThirdtImg)
    # # #
    Firstbtn = Button(root_v2, image=FirstImg,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn.grid(row=1,column=0,padx=5,sticky=W+S+N)
    Secondbtn = Button(root_v2, image=SecondtImg,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn.grid(row=1,column=2,padx=5,sticky=W+S+N)
    Thirdbtn = Button(root_v2, image=ThirdtImg,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    Thirdbtn.grid(row=1,column=4,padx=5,sticky=W+S+N)
    # row2
    NewMovLbl = Label(root_v2,text="原創 :")
    NewMovLbl.grid(row=2,column=0,sticky=W+S+N)
    # row3
    FirstImg_2 = Image.open("Project/Pic/soul.jpg")
    FirstImg_2 = FirstImg_2.resize((150,200))
    FirstImg_2 = ImageTk.PhotoImage(FirstImg_2)
    SecondtImg_2 = Image.open("Project/Pic/turning.jpg")
    SecondtImg_2 = SecondtImg_2.resize((150,200))
    SecondtImg_2 = ImageTk.PhotoImage(SecondtImg_2)
    ThirdtImg_2 = Image.open("Project/Pic/rat.jpg")
    ThirdtImg_2 = ThirdtImg_2.resize((150,200))
    ThirdtImg_2 = ImageTk.PhotoImage(ThirdtImg_2)
    # # #
    Firstbtn_2 = Button(root_v2, image=FirstImg_2,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn_2.grid(row=3,column=0,padx=5,sticky=W+S+N)
    Secondbtn_2 = Button(root_v2, image=SecondtImg_2,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn_2.grid(row=3,column=2,padx=5,sticky=W+S+N)
    Thirdbtn_2 = Button(root_v2, image=ThirdtImg_2,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    Thirdbtn_2.grid(row=3,column=4,padx=5,sticky=W+S+N)
    # row4
    NewMovLbl_1 = Label(root_v2,text="電影 :")
    NewMovLbl_1.grid(row=4,column=0,sticky=W+S+N)
    # row5
    FirstImg_3 = Image.open("Project/Pic/toy3.jpg")
    FirstImg_3 = FirstImg_3.resize((150,200))
    FirstImg_3 = ImageTk.PhotoImage(FirstImg_3)
    SecondtImg_3 = Image.open("Project/Pic/walle.jpg")
    SecondtImg_3 = SecondtImg_3.resize((150,200))
    SecondtImg_3 = ImageTk.PhotoImage(SecondtImg_3)
    ThirdtImg_3 = Image.open("Project/Pic/Power.jpg")
    ThirdtImg_3 = ThirdtImg_3.resize((150,200))
    ThirdtImg_3 = ImageTk.PhotoImage(ThirdtImg_3)
    # # #
    Firstbtn_3 = Button(root_v2, image=FirstImg_3,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn_3.grid(row=5,column=0,padx=5,sticky=W+S+N)
    Secondbtn_3 = Button(root_v2, image=SecondtImg_3,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn_3.grid(row=5,column=2,padx=5,sticky=W+S+N)
    Thirdbtn_3 = Button(root_v2, image=ThirdtImg_3,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    Thirdbtn_3.grid(row=5,column=4,padx=5,sticky=W+S+N)

    root_v2.mainloop()

# # Marvel
def Marvel():
    root_v2 = Toplevel() 
    root_v2.title("Marvel")
    root_v2.geometry("500x700+150+0")
    # row0
    NiceMovLbl = Label(root_v2,text="精選 :")
    NiceMovLbl.grid(row=0,column=0,sticky=W+S+N)
    # row1
    FirstImg = Image.open("Project/Pic/Strange.jpg")
    FirstImg = FirstImg.resize((150,200))
    FirstImg = ImageTk.PhotoImage(FirstImg)
    SecondtImg = Image.open("Project/Pic/ShanChi.jpg")
    SecondtImg = SecondtImg.resize((150,200))
    SecondtImg = ImageTk.PhotoImage(SecondtImg)
    ThirdtImg = Image.open("Project/Pic/黑豹2.jpg")
    ThirdtImg = ThirdtImg.resize((150,200))
    ThirdtImg = ImageTk.PhotoImage(ThirdtImg)
    # # #
    Firstbtn = Button(root_v2, image=FirstImg,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn.grid(row=1,column=0,padx=5,sticky=W+S+N)
    Secondbtn = Button(root_v2, image=SecondtImg,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn.grid(row=1,column=2,padx=5,sticky=W+S+N)
    Thirdbtn = Button(root_v2, image=ThirdtImg,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    Thirdbtn.grid(row=1,column=4,padx=5,sticky=W+S+N)
    # row2
    NewMovLbl = Label(root_v2,text="星際異攻隊 :")
    NewMovLbl.grid(row=2,column=0,sticky=W+S+N)
    # row3
    FirstImg_2 = Image.open("Project/Pic/GotG_1.jpg")
    FirstImg_2 = FirstImg_2.resize((150,200))
    FirstImg_2 = ImageTk.PhotoImage(FirstImg_2)
    SecondtImg_2 = Image.open("Project/Pic/Thor_LoveLightning.jpg")
    SecondtImg_2 = SecondtImg_2.resize((150,200))
    SecondtImg_2 = ImageTk.PhotoImage(SecondtImg_2)
    ThirdtImg_2 = Image.open("Project/Pic/EndGame.jpg")
    ThirdtImg_2 = ThirdtImg_2.resize((150,200))
    ThirdtImg_2 = ImageTk.PhotoImage(ThirdtImg_2)
    # # #
    Firstbtn_2 = Button(root_v2, image=FirstImg_2,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn_2.grid(row=3,column=0,padx=5,sticky=W+S+N)
    Secondbtn_2 = Button(root_v2, image=SecondtImg_2,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn_2.grid(row=3,column=2,padx=5,sticky=W+S+N)
    Thirdbtn_2 = Button(root_v2, image=ThirdtImg_2,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    Thirdbtn_2.grid(row=3,column=4,padx=5,sticky=W+S+N)
    # row4
    NewMovLbl_1 = Label(root_v2,text="慢威電影宇宙第四階段 :")
    NewMovLbl_1.grid(row=4,column=0,sticky=W+S+N)
    # row5
    FirstImg_3 = Image.open("Project/Pic/WandaVision.jpg")
    FirstImg_3 = FirstImg_3.resize((150,200))
    FirstImg_3 = ImageTk.PhotoImage(FirstImg_3)
    SecondtImg_3 = Image.open("Project/Pic/Loki.jpg")
    SecondtImg_3 = SecondtImg_3.resize((150,200))
    SecondtImg_3 = ImageTk.PhotoImage(SecondtImg_3)
    ThirdtImg_3 = Image.open("Project/Pic/BlackWidow.jpg")
    ThirdtImg_3 = ThirdtImg_3.resize((150,200))
    ThirdtImg_3 = ImageTk.PhotoImage(ThirdtImg_3)
    # # #
    Firstbtn_3 = Button(root_v2, image=FirstImg_3,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn_3.grid(row=5,column=0,padx=5,sticky=W+S+N)
    Secondbtn_3 = Button(root_v2, image=SecondtImg_3,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn_3.grid(row=5,column=2,padx=5,sticky=W+S+N)
    Thirdbtn_3 = Button(root_v2, image=ThirdtImg_3,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    Thirdbtn_3.grid(row=5,column=4,padx=5,sticky=W+S+N)

    root_v2.mainloop()

# # Star Wars
def StarWars():
    root_v2 = Toplevel() 
    root_v2.title("StarWars")
    root_v2.geometry("500x700+150+0")
    # row0
    NiceMovLbl = Label(root_v2,text="原創 :")
    NiceMovLbl.grid(row=0,column=0,sticky=W+S+N)
    # row1
    FirstImg = Image.open("Project/Pic/manda.jpg")
    FirstImg = FirstImg.resize((150,200))
    FirstImg = ImageTk.PhotoImage(FirstImg)
    SecondtImg = Image.open("Project/Pic/batch.jpg")
    SecondtImg = SecondtImg.resize((150,200))
    SecondtImg = ImageTk.PhotoImage(SecondtImg)
    ThirdtImg = Image.open("Project/Pic/boba.jpg")
    ThirdtImg = ThirdtImg.resize((150,200))
    ThirdtImg = ImageTk.PhotoImage(ThirdtImg)
    # # #
    Firstbtn = Button(root_v2, image=FirstImg,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn.grid(row=1,column=0,padx=5,sticky=W+S+N)
    Secondbtn = Button(root_v2, image=SecondtImg,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn.grid(row=1,column=2,padx=5,sticky=W+S+N)
    Thirdbtn = Button(root_v2, image=ThirdtImg,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    Thirdbtn.grid(row=1,column=4,padx=5,sticky=W+S+N)
    # row2
    NewMovLbl = Label(root_v2,text="電影 :")
    NewMovLbl.grid(row=2,column=0,sticky=W+S+N)
    # row3
    FirstImg_2 = Image.open("Project/Pic/skywalker.jpg")
    FirstImg_2 = FirstImg_2.resize((150,200))
    FirstImg_2 = ImageTk.PhotoImage(FirstImg_2)
    SecondtImg_2 = Image.open("Project/Pic/jedi.jpg")
    SecondtImg_2 = SecondtImg_2.resize((150,200))
    SecondtImg_2 = ImageTk.PhotoImage(SecondtImg_2)
    ThirdtImg_2 = Image.open("Project/Pic/force.jpg")
    ThirdtImg_2 = ThirdtImg_2.resize((150,200))
    ThirdtImg_2 = ImageTk.PhotoImage(ThirdtImg_2)
    # # #
    Firstbtn_2 = Button(root_v2, image=FirstImg_2,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn_2.grid(row=3,column=0,padx=5,sticky=W+S+N)
    Secondbtn_2 = Button(root_v2, image=SecondtImg_2,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn_2.grid(row=3,column=2,padx=5,sticky=W+S+N)
    Thirdbtn_2 = Button(root_v2, image=ThirdtImg_2,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    Thirdbtn_2.grid(row=3,column=4,padx=5,sticky=W+S+N)
    # row4
    NewMovLbl_1 = Label(root_v2,text="星際大戰 :")
    NewMovLbl_1.grid(row=4,column=0,sticky=W+S+N)
    # row5
    FirstImg_3 = Image.open("Project/Pic/menace.jpg")
    FirstImg_3 = FirstImg_3.resize((150,200))
    FirstImg_3 = ImageTk.PhotoImage(FirstImg_3)
    SecondtImg_3 = Image.open("Project/Pic/clones.jpg")
    SecondtImg_3 = SecondtImg_3.resize((150,200))
    SecondtImg_3 = ImageTk.PhotoImage(SecondtImg_3)
    ThirdtImg_3 = Image.open("Project/Pic/clones2.jpg")
    ThirdtImg_3 = ThirdtImg_3.resize((150,200))
    ThirdtImg_3 = ImageTk.PhotoImage(ThirdtImg_3)
    # # #
    Firstbtn_3 = Button(root_v2, image=FirstImg_3,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn_3.grid(row=5,column=0,padx=5,sticky=W+S+N)
    Secondbtn_3 = Button(root_v2, image=SecondtImg_3,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn_3.grid(row=5,column=2,padx=5,sticky=W+S+N)
    Thirdbtn_3 = Button(root_v2, image=ThirdtImg_3,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    Thirdbtn_3.grid(row=5,column=4,padx=5,sticky=W+S+N)

    root_v2.mainloop()

# # NG
def NG():
    root_v2 = Toplevel() 
    root_v2.title("National Geography")
    root_v2.geometry("400x700+150+0")
    # row0
    NiceMovLbl = Label(root_v2,text="精選 :")
    NiceMovLbl.grid(row=0,column=0,sticky=W+S+N)
    # row1
    FirstImg = Image.open("Project/Pic/hitler.jpg")
    FirstImg = FirstImg.resize((150,200))
    FirstImg = ImageTk.PhotoImage(FirstImg)
    SecondtImg = Image.open("Project/Pic/flight.jpg")
    SecondtImg = SecondtImg.resize((150,200))
    SecondtImg = ImageTk.PhotoImage(SecondtImg)
    # ThirdtImg = Image.open("Project/Pic/黑豹2.jpg")
    # ThirdtImg = ThirdtImg.resize((150,200))
    # ThirdtImg = ImageTk.PhotoImage(ThirdtImg)
    # # #
    Firstbtn = Button(root_v2, image=FirstImg,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn.grid(row=1,column=0,padx=5,sticky=W+S+N)
    Secondbtn = Button(root_v2, image=SecondtImg,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn.grid(row=1,column=2,padx=5,sticky=W+S+N)
    # Thirdbtn = Button(root_v2, image=ThirdtImg,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    # Thirdbtn.grid(row=1,column=4,padx=5,sticky=W+S+N)
    # row2
    NewMovLbl = Label(root_v2,text="原創 :")
    NewMovLbl.grid(row=2,column=0,sticky=W+S+N)
    # row3
    FirstImg_2 = Image.open("Project/Pic/space.jpg")
    FirstImg_2 = FirstImg_2.resize((150,200))
    FirstImg_2 = ImageTk.PhotoImage(FirstImg_2)
    SecondtImg_2 = Image.open("Project/Pic/challenge.jpg")
    SecondtImg_2 = SecondtImg_2.resize((150,200))
    SecondtImg_2 = ImageTk.PhotoImage(SecondtImg_2)
    # ThirdtImg_2 = Image.open("Project/Pic/EndGame.jpg")
    # ThirdtImg_2 = ThirdtImg_2.resize((150,200))
    # ThirdtImg_2 = ImageTk.PhotoImage(ThirdtImg_2)
    # # #
    Firstbtn_2 = Button(root_v2, image=FirstImg_2,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn_2.grid(row=3,column=0,padx=5,sticky=W+S+N)
    Secondbtn_2 = Button(root_v2, image=SecondtImg_2,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn_2.grid(row=3,column=2,padx=5,sticky=W+S+N)
    # Thirdbtn_2 = Button(root_v2, image=ThirdtImg_2,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    # Thirdbtn_2.grid(row=3,column=4,padx=5,sticky=W+S+N)
    # row4
    NewMovLbl_1 = Label(root_v2,text="影集、電影 :")
    NewMovLbl_1.grid(row=4,column=0,sticky=W+S+N)
    # row5
    FirstImg_3 = Image.open("Project/Pic/hitler2.jpg")
    FirstImg_3 = FirstImg_3.resize((150,200))
    FirstImg_3 = ImageTk.PhotoImage(FirstImg_3)
    SecondtImg_3 = Image.open("Project/Pic/bomb.jpg")
    SecondtImg_3 = SecondtImg_3.resize((150,200))
    SecondtImg_3 = ImageTk.PhotoImage(SecondtImg_3)
    # ThirdtImg_3 = Image.open("Project/Pic/BlackWidow.jpg")
    # ThirdtImg_3 = ThirdtImg_3.resize((150,200))
    # ThirdtImg_3 = ImageTk.PhotoImage(ThirdtImg_3)
    # # #
    Firstbtn_3 = Button(root_v2, image=FirstImg_3,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn_3.grid(row=5,column=0,padx=5,sticky=W+S+N)
    Secondbtn_3 = Button(root_v2, image=SecondtImg_3,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn_3.grid(row=5,column=2,padx=5,sticky=W+S+N)
    # Thirdbtn_3 = Button(root_v2, image=ThirdtImg_3,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    # Thirdbtn_3.grid(row=5,column=4,padx=5,sticky=W+S+N)

    root_v2.mainloop()

# # Star
def Star():
    root_v2 = Toplevel() 
    root_v2.title("Disney")
    root_v2.geometry("500x700+150+0")
    # row0
    NiceMovLbl = Label(root_v2,text="精選 :")
    NiceMovLbl.grid(row=0,column=0,sticky=W+S+N)
    # row1
    FirstImg = Image.open("Project/Pic/family.jpg")
    FirstImg = FirstImg.resize((150,200))
    FirstImg = ImageTk.PhotoImage(FirstImg)
    SecondtImg = Image.open("Project/Pic/spy.jpg")
    SecondtImg = SecondtImg.resize((150,200))
    SecondtImg = ImageTk.PhotoImage(SecondtImg)
    ThirdtImg = Image.open("Project/Pic/escape.jpg")
    ThirdtImg = ThirdtImg.resize((150,200))
    ThirdtImg = ImageTk.PhotoImage(ThirdtImg)
    # # #
    Firstbtn = Button(root_v2, image=FirstImg,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn.grid(row=1,column=0,padx=5,sticky=W+S+N)
    Secondbtn = Button(root_v2, image=SecondtImg,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn.grid(row=1,column=2,padx=5,sticky=W+S+N)
    Thirdbtn = Button(root_v2, image=ThirdtImg,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    Thirdbtn.grid(row=1,column=4,padx=5,sticky=W+S+N)
    # row2
    NewMovLbl = Label(root_v2,text="近期 :")
    NewMovLbl.grid(row=2,column=0,sticky=W+S+N)
    # row3
    FirstImg_2 = Image.open("Project/Pic/dead.jpg")
    FirstImg_2 = FirstImg_2.resize((150,200))
    FirstImg_2 = ImageTk.PhotoImage(FirstImg_2)
    SecondtImg_2 = Image.open("Project/Pic/take.jpg")
    SecondtImg_2 = SecondtImg_2.resize((150,200))
    SecondtImg_2 = ImageTk.PhotoImage(SecondtImg_2)
    ThirdtImg_2 = Image.open("Project/Pic/about.jpg")
    ThirdtImg_2 = ThirdtImg_2.resize((150,200))
    ThirdtImg_2 = ImageTk.PhotoImage(ThirdtImg_2)
    # # #
    Firstbtn_2 = Button(root_v2, image=FirstImg_2,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn_2.grid(row=3,column=0,padx=5,sticky=W+S+N)
    Secondbtn_2 = Button(root_v2, image=SecondtImg_2,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn_2.grid(row=3,column=2,padx=5,sticky=W+S+N)
    Thirdbtn_2 = Button(root_v2, image=ThirdtImg_2,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    Thirdbtn_2.grid(row=3,column=4,padx=5,sticky=W+S+N)
    # row4
    NewMovLbl_1 = Label(root_v2,text="動畫 :")
    NewMovLbl_1.grid(row=4,column=0,sticky=W+S+N)
    # row5
    FirstImg_3 = Image.open("Project/Pic/ball.jpg")
    FirstImg_3 = FirstImg_3.resize((150,200))
    FirstImg_3 = ImageTk.PhotoImage(FirstImg_3)
    SecondtImg_3 = Image.open("Project/Pic/stone.jpg")
    SecondtImg_3 = SecondtImg_3.resize((150,200))
    SecondtImg_3 = ImageTk.PhotoImage(SecondtImg_3)
    ThirdtImg_3 = Image.open("Project/Pic/black.jpg")
    ThirdtImg_3 = ThirdtImg_3.resize((150,200))
    ThirdtImg_3 = ImageTk.PhotoImage(ThirdtImg_3)
    # # #
    Firstbtn_3 = Button(root_v2, image=FirstImg_3,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn_3.grid(row=5,column=0,padx=5,sticky=W+S+N)
    Secondbtn_3 = Button(root_v2, image=SecondtImg_3,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn_3.grid(row=5,column=2,padx=5,sticky=W+S+N)
    Thirdbtn_3 = Button(root_v2, image=ThirdtImg_3,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    Thirdbtn_3.grid(row=5,column=4,padx=5,sticky=W+S+N)

    root_v2.mainloop()
"""
    # row6
    NewMovLbl_2 = Label(root_v2,text="慢威電影宇宙第三階段 :")
    NewMovLbl_2.grid(row=6,column=0,sticky=W+S+N)
    # row7
    FirstImg_4 = Image.open("Project/Pic/Strange.jpg")
    FirstImg_4 = FirstImg_4.resize((150,200))
    FirstImg_4 = ImageTk.PhotoImage(FirstImg_4)
    SecondtImg_4 = Image.open("Project/Pic/ShanChi.jpg")
    SecondtImg_4 = SecondtImg_4.resize((150,200))
    SecondtImg_4 = ImageTk.PhotoImage(SecondtImg_4)
    ThirdtImg_4 = Image.open("Project/Pic/黑豹2.jpg")
    ThirdtImg_4 = ThirdtImg_4.resize((150,200))
    ThirdtImg_4 = ImageTk.PhotoImage(ThirdtImg_4)
    # # #
    Firstbtn_4 = Button(root_v2, image=FirstImg_4,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn_4.grid(row=7,column=0,padx=5,sticky=W+S+N)
    Secondbtn_4 = Button(root_v2, image=SecondtImg_4,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn_4.grid(row=7,column=2,padx=5,sticky=W+S+N)
    Thirdbtn_4 = Button(root_v2, image=ThirdtImg_4,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    Thirdbtn_4.grid(row=7,column=4,padx=5,sticky=W+S+N)
    # row8
    NewMovLbl_3 = Label(root_v2,text="慢威電影宇宙第二階段 :")
    NewMovLbl_3.grid(row=8,column=0,sticky=W+S+N)
    # row9
    FirstImg_5 = Image.open("Project/Pic/Strange.jpg")
    FirstImg_5 = FirstImg_5.resize((150,200))
    FirstImg_5 = ImageTk.PhotoImage(FirstImg_5)
    SecondtImg_5 = Image.open("Project/Pic/ShanChi.jpg")
    SecondtImg_5 = SecondtImg_5.resize((150,200))
    SecondtImg_5 = ImageTk.PhotoImage(SecondtImg_5)
    ThirdtImg_5 = Image.open("Project/Pic/黑豹2.jpg")
    ThirdtImg_5 = ThirdtImg_5.resize((150,200))
    ThirdtImg_5 = ImageTk.PhotoImage(ThirdtImg_5)
    # # #
    Firstbtn = Button(root_v2, image=FirstImg_5,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn.grid(row=9,column=0,padx=5,sticky=W+S+N)
    Secondbtn = Button(root_v2, image=SecondtImg_5,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn.grid(row=9,column=2,padx=5,sticky=W+S+N)
    Thirdbtn = Button(root_v2, image=ThirdtImg_5,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    Thirdbtn.grid(row=9,column=4,padx=5,sticky=W+S+N)
    # row10
    NewMovLbl = Label(root_v2,text="慢威電影宇宙第一階段 :")
    NewMovLbl.grid(row=10,column=0,sticky=W+S+N)
    # row11
    FirstImg = Image.open("Project/Pic/Strange.jpg")
    FirstImg = FirstImg.resize((150,200))
    FirstImg = ImageTk.PhotoImage(FirstImg)
    SecondtImg = Image.open("Project/Pic/ShanChi.jpg")
    SecondtImg = SecondtImg.resize((150,200))
    SecondtImg = ImageTk.PhotoImage(SecondtImg)
    ThirdtImg = Image.open("Project/Pic/黑豹2.jpg")
    ThirdtImg = ThirdtImg.resize((150,200))
    ThirdtImg = ImageTk.PhotoImage(ThirdtImg)
    # # #
    Firstbtn = Button(root_v2, image=FirstImg,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
    Firstbtn.grid(row=11,column=0,padx=5,sticky=W+S+N)
    Secondbtn = Button(root_v2, image=SecondtImg,command=lambda:video("Project/Video/Leo2Mov.mp4"))
    Secondbtn.grid(row=11,column=2,padx=5,sticky=W+S+N)
    Thirdbtn = Button(root_v2, image=ThirdtImg,command=lambda:video("Project/Video/ShanChiMov.mp4"))
    Thirdbtn.grid(row=11,column=4,padx=5,sticky=W+S+N)
"""
# # root 
# row0
DisneyImage = Image.open("Project/Pic/Disney.jpg")
DisneyImage = DisneyImage.resize((480,300))
DisneyImage = ImageTk.PhotoImage(DisneyImage)
Disneybtn = Button(inner_frame, image=DisneyImage,command=Buy_Login,width=480,height=200)
Disneybtn.grid(row=0,column=0,columnspan=8,padx=0,sticky=N+S)

# row1
BannerImage = Image.open("Project/Pic/曼達.jpg")
BannerImage = BannerImage.resize((480,200))
BannerImage = ImageTk.PhotoImage(BannerImage)
BannerLabel = Label(inner_frame, image=BannerImage)
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
Disneybtn = Button(inner_frame, image=DisneyImg,command=Disney)
Disneybtn.grid(row=2,column=0,columnspan=2,padx=5,sticky=W)
PIXARbtn = Button(inner_frame, image=PIXARImg, command=Pixar)
PIXARbtn.grid(row=2,column=2,columnspan=2,padx=5,sticky=W+E)
Marvelbtn = Button(inner_frame, image=MarvelImg,command=Marvel)
Marvelbtn.grid(row=2,column=4,columnspan=2,padx=5,sticky=E)
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
SWbtn = Button(inner_frame, image=SWImg,command=StarWars)
SWbtn.grid(row=3,column=0,columnspan=2,padx=5,sticky=W)
NGbtn = Button(inner_frame, image=NGImg,command=NG)
NGbtn.grid(row=3,column=2,columnspan=2,padx=5,sticky=W+E)
Starbtn = Button(inner_frame, image=StarImg,command=Star)
Starbtn.grid(row=3,column=4,columnspan=2,padx=5,sticky=E)

# row4
FamousMovLbl = Label(inner_frame,text="熱門電影 :")
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

Drbtn = Button(inner_frame, image=DrImg,command=lambda:video("Project/Video/Dr.StrangeMov.mp4"))
Drbtn.grid(row=5,column=0,padx=5,sticky=W+S+N)
SCbtn = Button(inner_frame, image=SCImg,command=lambda:video("Project/Video/ShanChiMov.mp4"))
SCbtn.grid(row=5,column=2,padx=5,sticky=W+S+N)
Leobtn = Button(inner_frame, image=LeoImg,command=lambda:video("Project/Video/Leo2Mov.mp4"))
Leobtn.grid(row=5,column=4,padx=5,sticky=W+S+N)

# row6
SuggestMovLbl = Label(inner_frame,text="推薦給您 :")
SuggestMovLbl.grid(row=6,column=0,sticky=W+S+N)

# row7
GotGImg = Image.open("Project/Pic/GuardianOfTheGalaxy.jpg")
GotGImg = GotGImg.resize((150,200))
GotGImg = ImageTk.PhotoImage(GotGImg)
SpiderMan2Img = Image.open("Project/Pic/TheAmazing_2.jpg")
SpiderMan2Img = SpiderMan2Img.resize((150,200))
SpiderMan2Img = ImageTk.PhotoImage(SpiderMan2Img)
SpiderManFFHImg = Image.open("Project/Pic/SpiderManFFH.jpg")
SpiderManFFHImg = SpiderManFFHImg.resize((150,200))
SpiderManFFHImg = ImageTk.PhotoImage(SpiderManFFHImg)

GotGbtn = Button(inner_frame, image=GotGImg,command=lambda:video("Project/Video/GotG.mp4"))
GotGbtn.grid(row=7,column=0,padx=5,sticky=W+S+N)
SpiderMan2btn = Button(inner_frame, image=SpiderMan2Img,command=lambda:video("Project/Video/AmzaingSpiderMan2.mp4"))
SpiderMan2btn.grid(row=7,column=2,padx=5,sticky=W+S+N)
SpiderManFFHbtn = Button(inner_frame, image=SpiderManFFHImg,command=lambda:video("Project/Video/SpiderManFFH.mp4"))
SpiderManFFHbtn.grid(row=7,column=4,padx=5,sticky=W+S+N)

root.mainloop()