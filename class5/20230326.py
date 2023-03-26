# import MimeText
from email.mime.text import MIMEText
# If we need pic for the email, we need MimeImage and use pathlib to read the pic
from email.mime.image import MIMEImage
from pathlib import Path
# import MimeMultipart
from email.mime.multipart import MIMEMultipart
# 設定 Gmail 的 SMTP server 寄送
import smtplib

# MimeText
text = MIMEText(" Demo-Im an email from python")
# Use bytes for reading the pic
image = MIMEImage(Path("C:/Users/yoshi_pgnry07/Documents/Python_2023Spring/class1/logo_tree.png").read_bytes())
# MimeMultiPart
content = MIMEMultipart()
# Title
content["subject"] = "2023 python app 新程式春季班 <Demo>"
# 收件
content["from"] = "yoshilin77@gamil.com"
# 寄件
content["to"] = "kubetech.academy0524#gmail.com"
# content
content.attach(text)
# Img content
content.attach(image)
# smtplib
smtp = smtplib.SMTP(host="smtp.gmail.com", port="587")
# use with auto freed the resource
with open("C:/Users/yoshi_pgnry07/Documents/Python_2023Spring/class5/password.txt", "r") as f:
    mailToken = f.read()
with smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("yoshilin2.0@gmail.com", mailToken)
        smtp.send_message(content)
        print("The Email is Sended Completely!")
        smtp.quit()
    except Exception as e:
        print("Error Message: ",e)