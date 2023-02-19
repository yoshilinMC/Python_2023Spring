# 引入 Pillow module
from tkinter import *
from PIL import Image, ImageTk

root = Tk() 
root.title("Class1")
root.geometry("1000x300+150+150")

# 開啟圖片
img = Image.open("C:/Users/yoshi_pgnry07/Documents/Python_2023Spring/class1/logo_tree.png")
# 轉換為tk圖片物件
tk_img = ImageTk.PhotoImage(img)
# 設定程式icon
root.iconphoto(True,tk_img)

root.mainloop()