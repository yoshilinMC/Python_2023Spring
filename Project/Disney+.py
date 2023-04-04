from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
from tkscrolledframe import ScrolledFrame
from tkinter import ttk
from tkinter import filedialog
# import MimeText
from email.mime.text import MIMEText
# If we need pic for the email, we need MimeImage and use pathlib to read the pic
from email.mime.image import MIMEImage
from pathlib import Path
# import MimeMultipart
from email.mime.multipart import MIMEMultipart
# 設定 Gmail 的 SMTP server 寄送
import smtplib

root = Tk() 
root.title("Disney+")
root.geometry("500x650+150+150")

# row0
DisneyImage = Image.open("C:/Users/yoshi_pgnry07/Documents/Python_2023Spring/Project/Pic/Disney+.hpg.jpg")
DisneyImage = DisneyImage.resize((480,80))
DisneyImage = ImageTk.PhotoImage(DisneyImage)
DisneyLabel = Label(root, image=DisneyImage)
DisneyLabel.grid(row=0,column=0,columnspan=8,padx=5,sticky=W+N+S+E)

# row1
BannerImage = Image.open("C:/Users/yoshi_pgnry07/Documents/Python_2023Spring/Project/Pic/曼達.jpg")
BannerImage = BannerImage.resize((480,200))
BannerImage = ImageTk.PhotoImage(BannerImage)
BannerLabel = Label(root, image=BannerImage)
BannerLabel.grid(row=1,column=0,columnspan=8,padx=5,sticky=W+N+S+E)


root.mainloop()