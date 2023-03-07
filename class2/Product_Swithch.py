from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.ttk as ttk

root = Tk()
root.title("Switch Game")
root.geometry("880x650")

# def
def plus(NumLabel, PriceLabel):
    NumLabel["text"] = int(NumLabel["text"])+1
    Price = int(PriceLabel["text"].split(".")[1].strip())
    Total = int(Totalval.get().split(":")[1].replace("元","").strip())
    Totalval.set("共消費: "+str(Total+Price)+"元")
def minus(NumLabel, PriceLabel):
    if int(NumLabel["text"])>0:
        NumLabel["text"] = int(NumLabel["text"])-1
        Price = int(PriceLabel["text"].split(".")[1].strip())
        Total = int(Totalval.get().split(":")[1].replace("元","").strip())
        Totalval.set("共消費: "+str(Total-Price)+"元")
    else:
        messagebox.showwarning("showwarning", "The number of products can't be below 0")
def Login():
    LoginWindow = Toplevel(root)
    LoginWindow.geometry("280x200")
    LoginLabel = Label(LoginWindow, text="User Login")
    AcountLabel = Label(LoginWindow, text="Acount")
    PasswordLabel = Label(LoginWindow, text="Password")
    AcountEntry = Entry(LoginWindow)
    PasswordEntry = Entry(LoginWindow, show="*")
    LoginBtn = Button(LoginWindow, text="Login", width=10,command=lambda: verifyUser(LoginWindow, AcountEntry, PasswordEntry))
    LoginLabel.grid(row=0,column=0,columnspan=2,pady=5)
    AcountLabel.grid(row=1,column=0,sticky=W,padx=5)
    AcountEntry.grid(row=1,column=1,sticky=W+E+N+S)
    PasswordLabel.grid(row=2,column=0,sticky=W+E+N+S)
    PasswordEntry.grid(row=2,column=1,sticky=W+E+N+S)
    LoginBtn.grid(row=3,column=0,columnspan=2,pady=10)
def verifyUser(view,acountEntry,passwordEntry):
    if acountEntry.get()=="Yoshi" and passwordEntry.get()=="abcde":
        view.destroy()
    else:
        messagebox.showwarning("showwarning","This acount wasn't exist")
def CheckOut():
    CheckOut = Toplevel(root)
    CheckOut.geometry("280x200")
    LoginLabel = Label(CheckOut, text="User CheckOut")
    PasswordLabel = Label(CheckOut, text="Card Password")
    AcountEntry = Entry(CheckOut)
    PasswordEntry = Entry(CheckOut, show="*")
    LoginBtn = Button(CheckOut, text="Checkout", width=10,command=lambda: CheckOutUser(CheckOut, AcountEntry, PasswordEntry))
    LoginLabel.grid(row=0,column=0,columnspan=2,pady=5)
    PasswordLabel.grid(row=2,column=0,sticky=W+E+N+S)
    PasswordEntry.grid(row=2,column=1,sticky=W+E+N+S)
    LoginBtn.grid(row=3,column=0,columnspan=2,pady=10)
def CheckOutUser(view,acountEntry,passwordEntry):
    if passwordEntry.get()=="12345678" :
        view.destroy()
        root.destroy()
    else:
        messagebox.showwarning("showwarning","You can't use this card")
def Checking():
    Checking= Toplevel(root)
    Checking.geometry("1000x300")
    table = ttk.Treeview(Checking, columns=["Product Name", "Unit Price", "Quantity", "Subtotal"])
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
    subtotal1 = int(ProductPrice1Label["text"].split(".")[1].strip())*int(ProductNum1Label["text"])
    subtotal2 = int(ProductPrice2Label["text"].split(".")[1].strip())*int(ProductNum2Label["text"])
    subtotal3 = int(ProductPrice3Label["text"].split(".")[1].strip())*int(ProductNum3Label["text"])
    subtotal4 = int(ProductPrice4Label["text"].split(".")[1].strip())*int(ProductNum4Label["text"])
    table.insert("",index="end",text=ProductName1Label["text"],values=(ProductPrice1Label["text"],ProductNum1Label["text"],subtotal1))
    table.insert("",index="end",text=ProductName2Label["text"],values=(ProductPrice2Label["text"],ProductNum2Label["text"],subtotal2))
    table.insert("",index="end",text=ProductName3Label["text"],values=(ProductPrice3Label["text"],ProductNum3Label["text"],subtotal3))
    table.insert("",index="end",text=ProductName4Label["text"],values=(ProductPrice4Label["text"],ProductNum4Label["text"],subtotal4))
    table.insert("",index="end",text="total",values=(" "," ",subtotal4+subtotal1+subtotal2+subtotal3))
    # pack
    table.pack()
# Row0
# Switch Logo
TitleImage = Image.open("C:/Users/yoshi_pgnry07/OneDrive/桌面/Python_2022Autumn/Product/Pic/Switch_logo.jpg")
TitleImage = TitleImage.resize((50,50))
TitleImage = ImageTk.PhotoImage(TitleImage)
TitleLabel = Label(root, image=TitleImage)
TitleLabel.grid(row=0,column=0,sticky=W+N+S)
## 類型
# 動作
BattleGameButton = Button(root, text="戰鬥", pady=1, padx=5,fg="#1E1E1E",bg="#ECE8E7",width=5,height=2, font=("Inter",12))
# 射擊
ShootingGameButton = Button(root, text="射擊", pady=1, padx=5,fg="#1E1E1E",bg="#ECE8E7",width=5,height=2, font=("Inter",12))
# 角色扮演
CosplayGameButton = Button(root, text="RPG", pady=1, padx=5,fg="#1E1E1E",bg="#ECE8E7",width=5,height=2, font=("Inter",12))
# 競速
RacingGameButton = Button(root, text="競速", pady=1, padx=5,fg="#1E1E1E",bg="#ECE8E7",width=5,height=2, font=("Inter",12))
# 登入
SignUpButton = Button(root, text="會員登入/註冊", pady=1, padx=5,fg="#1E1E1E",bg="#F8DCDC",width=12,height=2, font=("Inter",12),command=Login)
# Print out
BattleGameButton.grid(row=0,column=1,sticky=E+W)
ShootingGameButton.grid(row=0,column=2,sticky=E+W)
CosplayGameButton.grid(row=0,column=3,sticky=E+W)
RacingGameButton.grid(row=0,column=4,sticky=E+W)
SignUpButton.grid(row=0,column=7,sticky=E+W)

# row1
BannerImage = Image.open("C:/Users/yoshi_pgnry07/Documents/Python_2023Spring/Pic/東森.jpg")

BannerImage = BannerImage.resize((852,298))
BannerImage = ImageTk.PhotoImage(BannerImage)
BannerLabel = Label(root, image=BannerImage)
BannerLabel.grid(row=1,column=0,columnspan=8,padx=5,sticky=W+N+S+E)

# row2
# Products
Sofa1Image = Image.open("C:/Users/yoshi_pgnry07/Documents/Python_2023Spring/Pic/任天堂明星大亂鬥.jpg")
Sofa1Image = Sofa1Image.resize((202,200))
Sofa1Image = ImageTk.PhotoImage(Sofa1Image)
Sofa2Image = Image.open("C:/Users/yoshi_pgnry07/Documents/Python_2023Spring/Pic/賽車.jpg")
Sofa2Image = Sofa2Image.resize((202,200))
Sofa2Image = ImageTk.PhotoImage(Sofa2Image)
Sofa3Image = Image.open("C:/Users/yoshi_pgnry07/Documents/Python_2023Spring/Pic/漆彈大作戰.jpg")
Sofa3Image = Sofa3Image.resize((202,200))
Sofa3Image = ImageTk.PhotoImage(Sofa3Image)
Sofa4Image = Image.open("C:/Users/yoshi_pgnry07/Documents/Python_2023Spring/Pic/薩爾達傳說.jpg")
Sofa4Image = Sofa4Image.resize((202,200))
Sofa4Image = ImageTk.PhotoImage(Sofa4Image)

Sofa1Label = Label(root, image=Sofa1Image)
Sofa1Label.grid(row=2,column=0,columnspan=2,padx=5,sticky=W)
Sofa2Label = Label(root, image=Sofa2Image)
Sofa2Label.grid(row=2,column=2,columnspan=2,padx=5,sticky=W)
Sofa3Label = Label(root, image=Sofa3Image)
Sofa3Label.grid(row=2,column=4,columnspan=2,padx=5,sticky=W)
Sofa4Label = Label(root, image=Sofa4Image)
Sofa4Label.grid(row=2,column=6,columnspan=2,padx=5,sticky=W)

# row3
# Product Name
ProductName1Label = Label(root, text="任天堂明星大亂鬥", pady=2, padx=5,fg="#000000", font=("Inter",10))
ProductName2Label = Label(root, text="馬力歐賽車", pady=2, padx=5,fg="#000000", font=("Inter",10))
ProductName3Label = Label(root, text="漆彈大作戰", pady=2, padx=5,fg="#000000", font=("Inter",10))
ProductName4Label = Label(root, text="薩爾達傳說", pady=2, padx=5,fg="#000000", font=("Inter",10))
ProductName1Label.grid(row=3,column=0,columnspan=2,sticky=W)
ProductName2Label.grid(row=3,column=2,columnspan=2,sticky=W)
ProductName3Label.grid(row=3,column=4,columnspan=2,sticky=W)
ProductName4Label.grid(row=3,column=6,columnspan=2,sticky=W)

# row4
# Product Price
ProductPrice1Label = Label(root, text="NT.1200", pady=2, padx=5,fg="#000000", font=("Inter",10))
ProductPrice2Label = Label(root, text="NT.1000", pady=2, padx=5,fg="#000000", font=("Inter",10))
ProductPrice3Label = Label(root, text="NT.2100", pady=2, padx=5,fg="#000000", font=("Inter",10))
ProductPrice4Label = Label(root, text="NT.2000", pady=2, padx=5,fg="#000000", font=("Inter",10))
ProductPrice1Label.grid(row=4,column=0,padx=5,sticky=W)
ProductPrice2Label.grid(row=4,column=2,padx=5,sticky=W)
ProductPrice3Label.grid(row=4,column=4,padx=5,sticky=W)
ProductPrice4Label.grid(row=4,column=6,padx=5,sticky=W)
# Product Number
ProductNum1Label = Label(root, text="0", pady=2, padx=5,fg="#000000", font=("Inter",12))
ProductNum2Label = Label(root, text="0", pady=2, padx=5,fg="#000000", font=("Inter",12))
ProductNum3Label = Label(root, text="0", pady=2, padx=5,fg="#000000", font=("Inter",12))
ProductNum4Label = Label(root, text="0", pady=2, padx=5,fg="#000000", font=("Inter",12))
# Product Minus
ProductMinus1 = Button(root, text="-", bg="#E7E2E2",fg="#1E1E1E",font=("Inter",10), command=lambda: minus(ProductNum1Label, ProductPrice1Label))
ProductMinus2 = Button(root, text="-", bg="#E7E2E2",fg="#1E1E1E",font=("Inter",10), command=lambda: minus(ProductNum2Label, ProductPrice2Label))
ProductMinus3 = Button(root, text="-", bg="#E7E2E2",fg="#1E1E1E",font=("Inter",10), command=lambda: minus(ProductNum3Label, ProductPrice3Label))
ProductMinus4 = Button(root, text="-", bg="#E7E2E2",fg="#1E1E1E",font=("Inter",10), command=lambda: minus(ProductNum4Label, ProductPrice4Label))
# Product Plus
ProductPlus1 = Button(root, text="+", bg="#E7E2E2",fg="#1E1E1E",font=("Inter",10), command=lambda: plus(ProductNum1Label, ProductPrice1Label))
ProductPlus2 = Button(root, text="+", bg="#E7E2E2",fg="#1E1E1E",font=("Inter",10), command=lambda: plus(ProductNum2Label, ProductPrice2Label))
ProductPlus3 = Button(root, text="+", bg="#E7E2E2",fg="#1E1E1E",font=("Inter",10), command=lambda: plus(ProductNum3Label, ProductPrice3Label))
ProductPlus4 = Button(root, text="+", bg="#E7E2E2",fg="#1E1E1E",font=("Inter",10), command=lambda: plus(ProductNum4Label, ProductPrice4Label))
# Print out
ProductMinus1.grid(row=4,column=1,sticky=W)
ProductNum1Label.grid(row=4,column=1,sticky=W+E+S+N)
ProductPlus1.grid(row=4,column=1,sticky=E)
ProductMinus2.grid(row=4,column=3,sticky=W)
ProductNum2Label.grid(row=4,column=3,sticky=W+E+S+N)
ProductPlus2.grid(row=4,column=3,sticky=E)
ProductMinus3.grid(row=4,column=5,sticky=W)
ProductNum3Label.grid(row=4,column=5,sticky=W+E+S+N)
ProductPlus3.grid(row=4,column=5,sticky=E)
ProductMinus4.grid(row=4,column=7,sticky=W)
ProductNum4Label.grid(row=4,column=7,sticky=W+E+S+N)
ProductPlus4.grid(row=4,column=7,sticky=E)

# row5
# Row Config
root.rowconfigure(5, weight=2)
# Detail List
DetailListbtn = Button(root, text="詳細清單", bg="#ECEDE7",fg="#1E1E1E",font=("Inter",12),command=Checking)
DetailListbtn.grid(row=5,column=0,sticky=W+S,padx=5,pady=1)
# Shopping Cart
ShoppingCartImage = Image.open("C:/Users/yoshi_pgnry07/Documents/Python_2023Spring/Pic/Shopping Cart.png")
ShoppingCartImage = ShoppingCartImage.resize((30,30))
ShoppingCartImage = ImageTk.PhotoImage(ShoppingCartImage)
ShoppingCartLabel = Label(root, image=ShoppingCartImage)
ShoppingCartLabel.grid(row=5,column=4,sticky=E+S)
# Total Val
Totalval = StringVar()
Totalval.set("共消費:0元")
TotalLabel = Label(root, textvariable=Totalval, bg="#ECEDE7",fg="#1E1E1E", font=("Inter",12))
TotalLabel.grid(row=5,column=5,columnspan=2,sticky=S+W)
# Check Out
CheckOutButton = Button(root, text="結帳", bg="#ECEDE7",fg="#1E1E1E", font=("Inter",12),command=CheckOut)
CheckOutButton.grid(row=5,column=7,sticky=E+S)

root.mainloop()