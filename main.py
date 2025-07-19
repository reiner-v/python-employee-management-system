import os

import data
data.createFile() # create the file first

from tkinter import *
from tkinter import messagebox

import module as mod
ae = mod.Employee()
eRecord = ae.createDict()
emRecord = ae.createEMD()

window = Tk()
window.title("ABC COMPANY")
window.config(bg='white')

from images import *

icon = PhotoImage(file='icons/ABC.png')  # for icon
window.iconphoto(False,icon)

def showPage(page):
    page.tkraise()  # allows to call the frame that stacks in each other or switch each frame

# last frame is the first read (page5 or frame 5)
# Put in layer by layer thus the last frame was on the top
page1 = Frame(window,bg='white')  # Generate Employee
page2 = Frame(window,bg='white')  # Update Employee
page3 = Frame(window,bg='white')  # Add Employee
page4 = Frame(window,bg='white')  # Homepage

for page in (page1, page2, page3, page4):  # to put everyone in the window and can be called whenever
    page.grid(row=0, column=0, sticky="NSEW")

# ===================================================================================================PAGE3(Add Employee)
def newBtn(): # page3
    enEntryP3.delete('0', 'end')  # delete the character in the entry
    lnEntry.delete('0', 'end')
    fnEntry.delete('0', 'end')
    enEntryP3.config(fg='black')  # to return the text to black
    lnEntry.config(fg='black')
    fnEntry.config(fg='black')
    posBox.select_clear('0','end')  # deselect
    depBox.select_clear('0','end')

def empSave(): # command; save button function
    ae.checkEN(enEntryP3)  # call function to check the entry in employee number
    ae.checkName(fnEntry,lnEntry)   # call function: check name entry
    position = ae.getPosition(posBox)  # call function: get position then return position
    department = ae.getDepartment(depBox)  # call function: get department

    if position == 'Manager':  # to check the availability of a specific position
        txt = ae.availablePosition(position,department)
        if txt != "":
            messagebox.showerror("ABC COMPANY",txt)
            return
    elif position == 'Assitant Manager':
        txt = ae.availablePosition(position,department)
        if txt != "":
            messagebox.showerror("ABC COMPANY", txt)
            return
    elif position == 'Secretary':
        txt = ae.availablePosition(position,department)
        if txt != "":
            messagebox.showerror("ABC COMPANY",txt)
            return
    elif position == 'Staff':
        txt = ae.availablePosition(position,department)
        if txt != "":
            messagebox.showerror("ABC COMPANY",txt)
            return

    ae.bdate(mmBox,dyBox,yrBox)
    ae.getRpd()

    txt = ae.writeEmp(enEntryP3)  # call function: to save in file
    if txt == "This Employee already exist":  # to control what to show if error or info
        messagebox.showerror("ABC COMPANY", txt)
    elif txt == "Successfully Added":
        messagebox.showinfo("ABC COMPANY", txt)
        ae.createDict()  # after adding it would write again in the dictionary
        newBtn()

whitesmoke ='#F5F5F5'
smokeyblack = '#333333'

Label(page3,image=aEmployee,bg='white').grid(row=1,column=0,sticky='W',padx=110,pady=10)

addLabel = Label(page3, text="ADD EMPLOYEE", font="Times 15 bold",bg='white')
addLabel.grid(row=1,column=0, sticky='W', padx=160, pady=10)

enLabel = Label(page3, text="Employee No.:", font="Helvetica 10 bold",bg='white')  # Employee Number
enLabel.grid(row=2,column=0,sticky='W',padx=10,pady=10)
enEntryP3 = Entry(page3,bg=whitesmoke,selectbackground='black',highlightthickness=2,relief=GROOVE)
enEntryP3.grid(row=2, column=0, sticky='W', padx=110, pady=10)

lnLabel = Label(page3, text="Last Name:", font="Helvetica 10 bold",bg='white')  # Last Name
lnLabel.grid(row=3,column=0,sticky='W',padx=10,pady=5)
lnEntry = Entry(page3,bg=whitesmoke,selectbackground='black',highlightthickness=2,relief=GROOVE)
lnEntry.grid(row=3,column=0,sticky='W',padx=110,pady=5)

fnLabel = Label(page3, text="First Name:", font="Helvetica 10 bold",bg='white')  # first Name
fnLabel.grid(row=4,column=0,sticky='W',padx=10,pady=5)
fnEntry = Entry(page3,bg=whitesmoke,selectbackground='black',highlightthickness=2,relief=GROOVE)
fnEntry.grid(row=4,column=0,sticky='W',padx=110,pady=5)

bdLabel = Label(page3, text="Birthdate:", font="Helvetica 10 bold",bg='white')
bdLabel.grid(row=5,column=0,sticky='W',padx=10,pady=5)

mmLabel = Label(page3, text="MM:", font="Helvetica 10 italic bold",bg='white')
mmLabel.grid(row=5,column=0,sticky='W',padx=110,pady=5)
dyLabel = Label(page3, text="DD:", font="Helvetica 10 italic bold",bg='white')
dyLabel.grid(row=5,column=0,sticky='W',padx=190,pady=5)
yrLabel = Label(page3, text="YY:", font="Helvetica 10 italic bold",bg='white')
yrLabel.grid(row=5,column=0,sticky='W',padx=270,pady=5)

mmValue = StringVar()
dyValue = StringVar()
yrValue = StringVar()
# Text Variable holds the value while Wrap=True goes back after reaching the max
mmBox = Spinbox(page3,width=3,from_=1,to=12,textvariable=mmValue,wrap=True,
                bg=whitesmoke,selectbackground='black',highlightthickness=2,relief=GROOVE) # design
mmBox.grid(row=5,column=0,sticky='W',padx=145,pady=5)
dyBox = Spinbox(page3,width=3,from_=1, to=31,textvariable=dyValue,wrap=True,
                bg=whitesmoke,selectbackground='black',highlightthickness=2,relief=GROOVE) # design
dyBox.grid(row=5,column=0,sticky='W',padx=220,pady=5)
yrBox = Spinbox(page3,width=6,from_=1995,to=2022,textvariable=yrValue,wrap=True,
                bg=whitesmoke,selectbackground='black',highlightthickness=2,relief=GROOVE) # design
yrBox.grid(row=5,column=0,sticky='W',padx=300,pady=5)

# =====================position===============================
posLabel = Label(page3, text="Position", font="Helvetica 10 bold",bg='white')
posLabel.grid(row=6,column=0,sticky='W',padx=10,pady=5)

posBox = Listbox(page3, width=20,height=4,selectmode=SINGLE,exportselection=0,
                 selectbackground="black",font='Helvetica 10',bg=whitesmoke,highlightthickness=2,relief=GROOVE)
posBox.grid(row=7,column=0,sticky='W',padx=30)

position = ['Manager','Assistant Manager','Secretary','Staff']
x = 0
for p in position:
    posBox.insert(x,p)
    x+=1

# =====================department===============================
depLabel = Label(page3, text="Department", font="Helvetica 10 bold",bg='white')
depLabel.grid(row=6,column=0,sticky='W',padx=200)
depBox = Listbox(page3, width=20, height=5, selectmode=SINGLE,exportselection=0,
                 selectbackground="black",font='Helvetica 10',bg=whitesmoke,highlightthickness=2,relief=GROOVE)
depBox.grid(row=7,column=0,sticky='W',padx=220)

department = ['Accounting','Sales and Marketing','Human Resources','Manufacturing','Admin']
c = 0
for d in department:
    depBox.insert(c,d)
    c+=1

# ================================Buttons===============================
btnNew = Button(page3,text="New",font="Helvetica 9 bold",width=10, pady=5,relief=RAISED,bg=smokeyblack,fg='white',
                command=newBtn)
btnNew.grid(row=8,column=0,sticky='W',padx=360,pady=20)

btnSave = Button(page3, text="Save", font="Helvetica 9 bold", width=10, pady=5,relief=RAISED,bg=smokeyblack,fg='white',
                 command=empSave)
btnSave.grid(row=8,column=0,sticky='W',padx=280,pady=20)

btnBack = Button(page3, image=back,relief=FLAT,bg='white',command=lambda:showPage(page4))
btnBack.grid(row=9,column=0,sticky='W',padx=10,pady=70)

# =================================================================================================PAGE2(Update Payslip)
def aprWindow(): #To open another container when btnApr was clicked (Add Payroll)
    aprW = Toplevel(page2)
    aprW.title("ADD PAYROLL")
    aprW.iconphoto(False,icon)
    aprW.config(bg='white')

    Label(aprW,text="ADD PAYROLL",font="Times 15 bold",bg='white').grid(row=1,column=0,sticky='W',pady=10,padx=130)

    enLabel = Label(aprW, text="Employee No.:", font="Helvetica 10 bold",bg='white')
    enLabel.grid(row=2, column=0, sticky='W', padx=10, pady=10)
    enEntryAprW = Entry(aprW,bg=whitesmoke,selectbackground='black',highlightthickness=2,relief=GROOVE)
    enEntryAprW.grid(row=2, column=0, sticky='W', padx=110, pady=10)

    dateLabel = Label(aprW, text="Date:", font="Helvetica 10 bold",bg='white')
    dateLabel.grid(row=3, column=0, sticky='W', padx=10, pady=5)

    Label(aprW, text="MM:", font="Helvetica 10 italic bold",bg='white').grid(row=3, column=0, sticky='W', padx=80, pady=5)
    Label(aprW, text="DD:", font="Helvetica 10 italic bold", bg='white').grid(row=3, column=0, sticky='W', padx=160,pady=5)

    monthValue = StringVar()
    dayValue = StringVar()
    # Text Variable holds the value while Wrap=True goes back after reaching the max
    monthBox = Spinbox(aprW, width=3, from_=1, to=12, textvariable=monthValue,wrap=True,
                       bg=whitesmoke,selectbackground='black',highlightthickness=2,relief=GROOVE)
    monthBox.grid(row=3, column=0, sticky='W', padx=120, pady=5)
    dayBox = Spinbox(aprW, width=3, from_=1, to=31, textvariable=dayValue, wrap=True,
                     bg=whitesmoke,selectbackground='black',highlightthickness=2,relief=GROOVE)
    dayBox.grid(row=3, column=0, sticky='W', padx=200, pady=5)

    def addP():
        ae.checkEN(enEntryAprW)
        date = '\n'+ enEntryAprW.get() + ',' + monthBox.get() + ',' + dayBox.get()
        key = enEntryAprW.get()+'/'+str(monthBox.get())
        if enEntryAprW.get() not in eRecord.keys():
            messagebox.showerror('ADD PAYROLL','Invalid Input')
        else:
            if key not in emRecord.keys():  # to check if record of this month has already been recorded
                ae.AddPayroll(date, enEntryAprW)
                messagebox.showinfo('ADD PAYROLL','Successfully Added')
                enEntryAprW.config(fg='black')
                ae.createEMD() # to rewrite dictionary of monthly record
                return
            else:
                messagebox.showerror('ADD PAYROLL','There is a Record of this Month')
                return

    btnAddP = Button(aprW, text="ADD PAYROLL", font="Helvetica 10 bold", width=15, pady=5,
                     relief=RAISED,bg=smokeyblack,fg='white',command=addP)
    btnAddP.grid(row=4, column=0, sticky='W', padx=250, pady=30)

    aprW.geometry('400x200')
    aprW.mainloop()

def delWindow():
    def askyesorno():
        ask = messagebox.askyesno("Delete Employee", "Are you sure you want to delete?",) # title, message
        if ask: #if ask messagebox chose yes
            ae.checkEN(enEntrydelW)
            ae.delEN(enEntrydelW)
            ae.delMD(enEntrydelW)
            ae.rewriteEmp()
            messagebox.showinfo("Delete Employee","Successfully Deleted")
            return

    delW = Toplevel(window)
    delW.title("DELETE EMPLOYEE")
    delW.iconphoto(False, icon)
    delW.config(bg='white')

    Label(delW, text="DELETE EMPLOYEE", font="Times 15 bold",bg='white').grid(row=1, column=0, sticky='W', pady=10, padx=110)

    enLabel = Label(delW, text="Employee No. ", font="Helvetica 10 bold",bg='white')
    enLabel.grid(row=2, column=0, sticky='W', padx=10, pady=10)
    enEntrydelW = Entry(delW,bg=whitesmoke,selectbackground='black',highlightthickness=2,relief=GROOVE)
    enEntrydelW.grid(row=2, column=0, sticky='W', padx=110, pady=10)

    #===================Button=================
    btnDel = Button(delW, text="Delete", font="Helvetica 10 bold", width=8, pady=5,
                    relief=RAISED,bg=smokeyblack,fg='white', command=askyesorno)
    btnDel.grid(row=3, column=0, sticky='W', padx=305, pady=20)

    delW.geometry('400x160')
    delW.mainloop()

def clearEList():
    ask = messagebox.askyesno("Clear Record", "Do you want to Permanenty delete the Record?",) # title, message
    if ask: #if ask messagebox chose yes
        ae.clearList()
        os.remove('eList.txt')
        os.remove('EMList.txt')
        messagebox.showinfo("Clear Record","Successfully Cleared")
        return

def posWindow():
    def cPos():
        position = ae.getPosition(posB)
        try:
            department = eRecord[enEntryposW.get()]['Department']
        except KeyError:
            messagebox.showerror("CHANGE POSITION", 'Invalid Input')
            return
        if position == 'Manager':  # to check the availability of a specific position
            txt = ae.availablePosition(position,department)
            if txt != "":
                messagebox.showerror("ABC COMPANY", txt)
                return
        elif position == 'Assitant Manager':
            txt = ae.availablePosition(position,department)
            if txt != "":
                messagebox.showerror("ABC COMPANY", txt)
                return
        elif position == 'Secretary':
            txt = ae.availablePosition(position,department)
            if txt != "":
                messagebox.showerror("ABC COMPANY", txt)
                return
        elif position == 'Staff':
            txt = ae.availablePosition(position,department)
            if txt != "":
                messagebox.showerror("ABC COMPANY", txt)
                return
        eRecord[enEntryposW.get()]['Rate per day'] = ae.getRpd()
        eRecord[enEntryposW.get()]['Position'] = position
        ae.rewriteEmp()
        messagebox.showinfo("ABC COMPANY","Successfully Changed")
        posW.destroy()

    posW = Toplevel(window)
    posW.title("CHANGE POSITION")
    posW.config(bg='white')

    Label(posW,text="CHANGE POSITION",font="Times 15 bold",bg='white').grid(row=1,column=0,sticky='W',pady=10,padx=110)

    enLabel = Label(posW, text="Employee No. ", font="Helvetica 10 bold",bg='white')
    enLabel.grid(row=2, column=0, sticky='W', padx=10, pady=10)
    enEntryposW = Entry(posW,bg=whitesmoke,selectbackground='black',highlightthickness=2,relief=GROOVE)
    enEntryposW.grid(row=2, column=0, sticky='W', padx=110, pady=10)

    posL = Label(posW, text="Position ", font="Helvetica 10 bold",bg='white')
    posL.grid(row=3, column=0, sticky='W', padx=10, pady=10)
    posB = Listbox(posW, width=20, height=4, selectmode=SINGLE,exportselection=0,
                   selectbackground="black",font='Helvetica 10',bg=whitesmoke,highlightthickness=2,relief=GROOVE)
    posB.grid(row=3, column=0, sticky='W', padx=110, pady=5)

    x = 0
    for p in position:
        posB.insert(x, p)
        x += 1

    btnS = Button(posW, text="Save", font="Helvetica 10 bold", width=10, pady=5,
                  relief=RAISED,bg=smokeyblack,fg='white',command=cPos)
    btnS.grid(row=4, column=0, sticky='W', padx=300, pady=30)

    posW.geometry('400x250')
    posW.mainloop()

def depWindow():
    def cDep():
        position = eRecord[enEntrydepW.get()]['Position']
        department = ae.getDepartment(depB)
        if position == 'Manager':  # to check the availability of a specific position
            txt = ae.availablePosition(position,department)
            if txt != "":
                messagebox.showerror("ABC COMPANY", txt)
                return
        elif position == 'Assitant Manager':
            txt = ae.availablePosition(position,department)
            if txt != "":
                messagebox.showerror("ABC COMPANY", txt)
                return
        elif position == 'Secretary':
            txt = ae.availablePosition(position,department)
            if txt != "":
                messagebox.showerror("ABC COMPANY", txt)
                return
        elif position == 'Staff':
            txt = ae.availablePosition(position,department)
            if txt != "":
                messagebox.showerror("ABC COMPANY", txt)
                return
        eRecord[enEntrydepW.get()]['Department'] = department
        ae.rewriteEmp()
        messagebox.showinfo("ABC COMPANY","Successfully Changed")
        depW.destroy()

    depW = Toplevel(window)
    depW.title("CHANGE DEPARTMENT")
    depW.iconphoto(False, icon)
    depW.config(bg='white')

    Label(depW, text="CHANGE DEPARTMENT", font="Times 15 bold", bg='white').grid(row=1, column=0, sticky='W', pady=10, padx=90)

    enLabel = Label(depW, text="Employee No. ", font="Helvetica 10 bold",bg='white')
    enLabel.grid(row=2, column=0, sticky='W', padx=10, pady=10)
    enEntrydepW = Entry(depW,bg=whitesmoke,selectbackground='black',highlightthickness=2,relief=GROOVE)
    enEntrydepW.grid(row=2, column=0, sticky='W', padx=110, pady=10)

    enLabel = Label(depW, text="Department", font="Helvetica 10 bold",bg='white')
    enLabel.grid(row=3, column=0, sticky='W', padx=10, pady=10)
    depB = Listbox(depW, width=20, height=5, selectmode=SINGLE,exportselection=0,
                   selectbackground="black",font='Helvetica 10',bg=whitesmoke,highlightthickness=2,relief=GROOVE)
    depB.grid(row=3, column=0, sticky='W', padx=110, pady=5)

    c = 0
    for d in department:
        depB.insert(c, d)
        c += 1

    btnS = Button(depW, text="Save", font="Helvetica 10 bold", width=8, pady=5,
                  relief=RAISED,bg=smokeyblack,fg='white',command=cDep)
    btnS.grid(row=4, column=0, sticky='W', padx=320, pady=35)

    depW.geometry('400x270')
    depW.mainloop()

#==========================Buttons==============================
Label(page2,image=udEmployee,bg='white').grid(row=1,column=0,sticky='W',padx=98,pady=10)

udLabel = Label(page2, text="UPDATE EMPLOYEE", font="Times 15 bold",bg='white')
udLabel.grid(row=1,column=0, padx=150, pady=10)
btnAPR = Button(page2, text="ADD PAYROLL", font="Helvetica 10 bold", width=20, pady=5,
                relief=SUNKEN,borderwidth=5,command=aprWindow)
btnAPR.grid(row=2,column=0, pady=5,sticky='W',padx=140)
btncPos = Button(page2, text="CHANGE POSITION", font="Helvetica 10 bold", width=20, pady=5,
                 relief=SUNKEN,borderwidth=5,command=posWindow)
btncPos.grid(row=3,column=0, pady=5,sticky='W',padx=140)
btncDep = Button(page2, text="CHANGE DEPARTMENT", font="Helvetica 10 bold", width=20, pady=5,
                 relief=SUNKEN,borderwidth=5,command=depWindow)
btncDep.grid(row=4,column=0, pady=5,sticky='W',padx=140)
btnDelE = Button(page2, text="DELETE EMPLOYEE", font="Helvetica 10 bold", width=20, pady=5,
                 relief=SUNKEN,borderwidth=5,command=delWindow)
btnDelE.grid(row=5,column=0, pady=5,sticky='W',padx=140)
btnCE = Button(page2, text="CLEAR EMPLOYEE LIST", font="Helvetica 10 bold", width=20, pady=5,
               relief=SUNKEN,borderwidth=5,command=clearEList)
btnCE.grid(row=6,column=0, pady=5,sticky='W',padx=140)

btnBack = Button(page2,image=back,bg='white',relief=FLAT,command=lambda:showPage(page4))
btnBack.grid(row=7,column=0,pady=145,padx=10,sticky='W')
# ===================================================================================================(Increase Pay)
def incPayW():
    def increase():
        ae.increasePay(enEntryIP)
        ae.rewriteEmp()
        messagebox.showinfo("ABC COMPANY", 'Successfully Increase')

    ipWindow = Toplevel(page4)  # to make another window or container
    ipWindow.title('ABC COMPANY')
    ipWindow.iconphoto(False,icon)
    ipWindow.config(bg='white')

    Label(ipWindow, image=increasePay, bg='white').grid(row=1, column=0, sticky='W', padx=98, pady=10)

    genPLabel = Label(ipWindow, text="INCREASE PAY", font="Georgia 14 bold",bg='white')
    genPLabel.grid(row=1,column=0, sticky='W', padx=145, pady=10)

    enLabel = Label(ipWindow, text="Employee No. ", font="Helvetica 10 bold",bg='white')
    enLabel.grid(row=2,column=0,sticky='W',padx=10,pady=10)
    enEntryIP = Entry(ipWindow,bg=whitesmoke,selectbackground='black',highlightthickness=2,relief=GROOVE)
    enEntryIP.grid(row=2, column=0, sticky='W', padx=110, pady=10)

    btnInc = Button(ipWindow, text="Increase", font="Helvetica 10 bold", width=13, pady=5,
                    relief=RAISED,bg=smokeyblack,fg='white',command=increase)
    btnInc.grid(row=3,column=0,sticky='W',padx=280,pady=25)

    ipWindow.geometry('400x180')
    ipWindow.mainloop()

# ======================================================================================================PAGE1(Payslip)
def preview():
    prev = Toplevel(page2)
    prev.title("ABC COMPANY")
    prev.iconphoto(False, icon)
    Label(prev, image=logo, relief=FLAT).grid(row=0,column=0,sticky='W',padx=185,pady=10)

    try:
        Label(prev, text="ABC COMPANY", font="Times 18 bold").grid(row=0, column=0, sticky='W', pady=10, padx=235)
        Label(prev, text="Payslip of the Month: ", font="Helvetica 11 bold").grid(row=1, column=0, sticky='W', pady=5, padx=10)

        selectedMonth = "---"
        for sm in mBox.curselection():
            selectedMonth = mBox.get(sm)

        Label(prev, text=selectedMonth.upper(), font="Helvetica 12 ").grid(row=1, column=0, sticky='W', pady=5, padx=180)
        Label(prev, text="Employee No.: ", font="Helvetica 12 bold").grid(row=2, column=0, sticky='W', pady=5,padx=10)
        Label(prev, text=enEntryP1.get(), font="Helvetica 12").grid(row=2, column=0, sticky='W', pady=5, padx=135)
        Label(prev, text="Name:", font="Helvetica 12 bold").grid(row=2, column=0, sticky='W', pady=5, padx=350)
        firstN = eRecord[enEntryP1.get()]['First name']
        lastN  = eRecord[enEntryP1.get()]['Last name']
        Label(prev, text=firstN, font="Helvetica 12").grid(row=2, column=0, sticky='W', pady=5, padx=410)
        Label(prev, text=lastN, font="Helvetica 12").grid(row=2, column=0, sticky='W', pady=5, padx=460)
        Label(prev, text='Birthdate:', font="Helvetica 12 bold").grid(row=3, column=0, sticky='W', pady=5, padx=10)
        Label(prev, text=eRecord[enEntryP1.get()]['Birthdate'], font="Helvetica 12").grid(row=3, column=0, sticky='W',
                                                                                               pady=5, padx=100)
        Label(prev, text='Department:', font="Helvetica 12 bold").grid(row=4, column=0, sticky='W', pady=5, padx=10)
        Label(prev, text='Position:', font="Helvetica 12 bold").grid(row=4, column=0, sticky='W', pady=5, padx=350)
        Label(prev, text=eRecord[enEntryP1.get()]['Department'], font="Helvetica 12").grid(row=4, column=0, sticky='W',
                                                                                                pady=5, padx=120)
        Label(prev, text=eRecord[enEntryP1.get()]['Position'], font="Helvetica 12").grid(row=4, column=0, sticky='W',
                                                                                                pady=5, padx=430)
        Label(prev, text="Rate per day:", font="Helvetica 12 bold").grid(row=5, column=0, sticky='W',pady=5, padx=10)
        Label(prev, text=eRecord[enEntryP1.get()]['Rate per day'], font="Helvetica 12").grid(row=5, column=0, sticky='W',
                                                                                         pady=5, padx=130)
        Label(prev, text="No. of days of worked:", font="Helvetica 12 bold").grid(row=6, column=0, sticky='W', pady=10, padx=10)
        monthIndex = int(month.index(selectedMonth))+1

        Label(prev, text=emRecord[enEntryP1.get()+'/'+str(monthIndex)], font="Helvetica 12").grid(row=6, column=0, sticky='W',
                                                                                             pady=10, padx=200)
        salary = int(eRecord[enEntryP1.get()]['Rate per day']) * int(emRecord[enEntryP1.get() + '/' + str(monthIndex)])
        Label(prev, text="Salary for the Month:", font="Helvetica 12 bold").grid(row=7, column=0, sticky='W', pady=30, padx=10)
        s = "{:,}".format(salary)
        Label(prev, text=s, font="Helvetica 12").grid(row=7, column=0, sticky='W', pady=30, padx=180)

        prev.geometry('600x350')
        prev.mainloop()
    except KeyError:
        prev.destroy()
        messagebox.showerror("ABC COMPANY", "This has no Record") # for month and employee number
        return
    except ValueError:
        prev.destroy()
        messagebox.showerror("ABC COMPANY", "Please Enter a Month")
        return

def generate():
    selectedMonth = "---"
    for sm in mBox.curselection():
        selectedMonth = mBox.get(sm)

    try:
        ae.generatePS(selectedMonth,month,enEntryP1)
    except KeyError:
        messagebox.showerror("ABC COMPANY","This has no Record")
    except ValueError:
        messagebox.showerror("ABC COMPANY", "Please Enter Month")
    else:
        messagebox.showinfo("ABC COMPANY","Successfully Generated")

Label(page1,image=payslip,bg='white').grid(row=1,column=0,sticky='W',padx=90,pady=10)

psLabel = Label(page1, text="GENERATE PAYSLIP", font="Georgia 14 bold",bg='white')
psLabel.grid(row=1,column=0, sticky='W', padx=150, pady=10)


enLabelPS = Label(page1, text="Employee No. ", font="Helvetica 10 bold",bg='white')
enLabelPS.grid(row=2,column=0,sticky='W',padx=10,pady=10)
enEntryP1 = Entry(page1,bg=whitesmoke,selectbackground='black',highlightthickness=2,relief=GROOVE)
enEntryP1.grid(row=2, column=0, sticky='W', padx=110, pady=10)

mBox = Listbox(page1, width=20, height=4, selectmode=SINGLE,
               selectbackground="black",font="Helvetica 10",bg=whitesmoke,highlightthickness=2,relief=GROOVE)
mBox.grid(row=3, column=0, sticky='W', padx=110, pady=5)
mLabel = Label(page1, text="Month ", font="Helvetica 10 bold",bg='white')
mLabel.grid(row=3, column=0, sticky='W', padx=10, pady=10)

month = ['January', 'February', 'March', 'April','May', 'June', 'July', 'August', 'September','October','November', 'December']

x = 0
for m in month:
    mBox.insert(x, m)
x += 1


scroll = Scrollbar(page1)
scroll.grid(row=3,column=0,sticky='W',padx=258,ipady=5)
mBox.config(yscrollcommand=scroll.set)
scroll.config(command=mBox.yview)

btnGen = Button(page1, text="Generate", font="Helvetica 9 bold", width=10, pady=5,
                relief=RAISED,bg=smokeyblack,fg='white',command=generate) # generatePS
btnGen.grid(row=4,column=0, sticky='W',padx=270,pady=10)

btnPrv = Button(page1, text="Preview", font="Helvetica 9 bold", width=10, pady=5,
                relief=RAISED,bg=smokeyblack,fg='white',command=preview)
btnPrv.grid(row=4,column=0,sticky='W',padx=355,pady=10)

btnBack = Button(page1,image=back,relief=FLAT,bg='white', command=lambda:showPage(page4))
btnBack.grid(row=5,column=0,sticky='W',padx=10,pady=230)

# ======================================================================================================PAGE4(Home Page)
def exitWindow(): # destory the window when exited
    exit = messagebox.askyesno("EXIT","Do you want to Exit?")
    if exit:
        window.destroy()
    else:
        return

def information():  # name and OBE
    info = Toplevel(page4)
    info.title("Credits")
    info.config(bg='white')
    info.iconphoto(False, icon)

    Label(info,image=logo,bg='white').grid(row=0,column=0,sticky='W',padx=85,pady=10)
    Label(info,text='ABC COMPANY',font="Times 16 bold",bg='white').grid(row=0,column=0,sticky='W',padx=140,pady=10)
    Label(info,text="CREATED BY\nReiner Gabrielle R. Valdez\nIT101-L/B51",font="Helvetica 10 bold",bg='white').grid(row=1,column=0,sticky='W',padx=110,pady=10)
    Label(info, text='SUBMITTED TO\nAurelia Sharlene Delos Santos', font="Helvetica 10 bold", bg='white').grid(row=2, column=0, sticky='W', padx=100,pady=20)
    Label(info, text='FINAL OBE PROJECT\nMACHINE PROBLEM 3.1', font="Helvetica 9 bold", bg='white').grid(row=3,column=0,sticky='W',padx=135,pady=40)
    info.geometry('400x300')
    info.mainloop()

logoABC = Button(page4,image=logo,relief=FLAT,bg='white',command=information) # credit button or info
logoABC.grid(row=6,column=0,padx=15,pady=170,sticky='E')

comLabel = Label(page4, text="ABC COMPANY", font="Times 23 bold",bg='white')
comLabel.grid(row=1,column=0, padx=110, pady=15)

# Use lambda(Anonymous Function or no name) to call a function with a parameter
# So, when you call the function showframe it will raise the page in the parameter
btnAdd = Button(page4, text="ADD EMPLOYEE",font="Helvetica 10 bold",width=20,pady=5,
                relief=SUNKEN,borderwidth=5,command=lambda: showPage(page3))
btnAdd.grid(row=2,column=0, pady=5)
btnUD = Button(page4, text="UPDATE EMPLOYEE", font="Helvetica 10 bold", width=20, pady=5,
               relief=SUNKEN, borderwidth=5,
               command=lambda: showPage(page2))
btnUD.grid(row=3,column=0, pady=5)
btnIncPay = Button(page4, text="INCREASE PAY", font="Helvetica 10 bold", width=20, pady=5,
                   relief=SUNKEN, highlightbackground='white', borderwidth=5,
                   command=incPayW)
btnIncPay.grid(row=4,column=0, pady=5)
btnPaySlip = Button(page4, text="GENERATE PAYSLIP", font="Helvetica 10 bold", width=20, pady=5,
                    relief=SUNKEN, highlightbackground='white', borderwidth=5,
                    command=lambda: showPage(page1))
btnPaySlip.grid(row=5,column=0, pady=5)

logOutDisplay = Button(page4,image=logOut,relief=FLAT,bg='white',command=exitWindow) # credit button or info
logOutDisplay.grid(row=6,column=0,padx=15,pady=170,sticky='W')

window.geometry('450x510') # width x height
window.mainloop()