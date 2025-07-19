from PIL import Image,ImageTk

logoImg = Image.open('icons/ABC.png')
logoResize =logoImg.resize((50,45))
logo =ImageTk.PhotoImage(logoResize)

logOutImg = Image.open('icons/logout.png')
logOutResize =logOutImg.resize((20,20))
logOut =ImageTk.PhotoImage(logOutResize)

backImg = Image.open(r'icons/\back.png')
backResize =backImg.resize((25,25))
back =ImageTk.PhotoImage(backResize)
#=========================================page3
aeImg = Image.open(r'icons/addEmployee.png')
aeResize =aeImg.resize((50,45))
aEmployee =ImageTk.PhotoImage(aeResize)
#=========================================page2
udImg = Image.open(r'icons/update.png')
udResize =udImg.resize((50,45))
udEmployee =ImageTk.PhotoImage(udResize)
#=========================================Increase pay
icpImg = Image.open('icons/increase.png')
icpResize = icpImg.resize((50, 45))
increasePay = ImageTk.PhotoImage(icpResize)

#=========================================Page1
psImg = Image.open('icons\payslip.png')
psResize =psImg.resize((50,45))
payslip =ImageTk.PhotoImage(psResize)