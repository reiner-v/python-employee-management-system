class Employee(object):
    def __init__(self):
        self._eList = dict()
        self._emdList = dict()

    def createDict(self): # creating dictionary for access
        file = open("eList.txt", "r")
        fRead = file.read()
        student = fRead.split('\n')
        for s in student:
            data = s.split(',')
            self._eList[data[0]] = {
                'First name': data[2],
                'Last name': data[1],
                'Position': data[3],
                'Department': data[4],
                'Birthdate': data[5],
                'Rate per day': data[6]
            }
        file.close()
        return self._eList

    def checkEN(self,empNum):
        empN = empNum.get()  # employee Number
        if len(empN) != 9 or not empN.isdigit():  # checking employee number
                empNum.config(fg='red') # to identify that its wrong(change to red)
                return

    def checkName(self,fnEntry,lnEntry):
        self.fn = fnEntry.get()
        self.ln = lnEntry.get()
        if not self.fn.isalpha() and self.ln.isalpha():
            fnEntry.config(fg='red')  # to identify that its wrong(change to red)
        elif not self.ln.isalpha() and self.fn.isalpha():
            lnEntry.config(fg='red')
        elif not self.fn.isalpha() and not self.ln.isalpha():
            fnEntry.config(fg='red')
            lnEntry.config(fg='red')
        return

    def getPosition(self,posBox):  # list box position
        self.position = "---"
        for pos in posBox.curselection():  # to return the index or number that is selected;
            # condition: If the selected index or number (curselected) has been found it will stop looping
            self.position = posBox.get(pos)  # the get the element or value of the containing number or index
        return self.position

    def getDepartment(self,depBox):  # department list box
        self.department = "---"
        for dep in depBox.curselection():
            self.department = depBox.get(dep)

        return self.department

    def availablePosition(self,pos,dep):
        file = open('eList.txt', 'r')
        fRead = file.read()
        line = fRead.split('\n')
        for info in line:
            data = info.split(',')
            if data[3] != 'Staff':
                if pos == data[3] and dep == data[4]:
                    txt = "This Position is not available in this department"
                    file.close()
                    return txt
        txt = ""
        return txt

    def bdate(self,mmBox,dyBox,yrBox):
        self.birthdate = mmBox.get() + '-' + dyBox.get() + '-' + yrBox.get()

    def getRpd(self):
        self.rpd = '0'
        if self.position == 'Manager':
            self.rpd = '1000'
        elif self.position == 'Assistant Manager':
            self.rpd = '750'
        elif self.position == 'Secretary':
            self.rpd = '500'
        elif self.position == 'Staff':
            self.rpd = '475'
        return self.rpd

    def writeEmp(self, empNum):
        empN = empNum.get()
        eList = self._eList

        if empN in eList:
            txt = "This Employee already exist"
            return txt
        elif empN not in eList and len(empN) == 9 :
            employee = '\n' + empN + ',' + self.ln + ',' + self.fn + ',' + self.position + ',' + self.department + ',' + self.birthdate + ',' + self.rpd

            file = open('eList.txt', 'a')
            file.write(employee)
            file.close()

            txt = "Successfully Added"
            return txt

    def increasePay(self, empNum):
        eList = self._eList
        rpd = int(eList[empNum.get()]['Rate per day'])
        incRpd = rpd // 2
        newRpd = incRpd + rpd
        newRpd = str(newRpd)
        eList[empNum.get()]['Rate per day'] = newRpd

    def changePos(self,empNum,position):
        self._eList[empNum.get()]['Position'] = position.get()

    def rewriteEmp(self):
        eList = self._eList
        employee = []

        for EN, D in eList.items():
            line = "%s,%s,%s,%s,%s,%s,%s\n" % (
            EN, eList[EN]['Last name'], eList[EN]['First name'], eList[EN]['Position'],
            eList[EN]['Department'], eList[EN]['Birthdate'], eList[EN]['Rate per day'])
            employee.append(line)

        file = open("eList.txt", "w")
        for e in employee:
            if e != " ":
                file.write(e)

    def delEN(self, empNum):
        del self._eList[empNum.get()]

    def clearList(self):
        del self._eList
        del self._emdList

#=================================Payroll
    def createEMD(self):
        file = open("eMList.txt", "r")
        fRead = file.read()
        student = fRead.split('\n')
        for s in student:
            data = s.split(',')
            self._emdList[data[0] + '/' + data[1]] = data[2]  # EN/month: Days
        file.close()
        return self._emdList

    def AddPayroll(self, date, empNum):
        for EN in self._eList.keys():
            with open('emList.txt','a') as file:
                file.write(date)
                file.close()
                return


    def delMD(self,empNum):
        emd = []
        for k,d in self._emdList.items(): # change to list so you can del everthing with the empNum
            data = k.split('/')
            line = "%s,%s,%s\n" % (data[0], data[1], d)
            emd.append(line)

        x=0  # for index
        for emp in emd:
            if empNum.get() in emp: # find in the list a line with the employee number
                del emd[x] # delete the index or line
            x+=1 # adding the index after not finding and finding

        file = open("EMList.txt", "w")  # rewriting
        for e in emd:
            if e != " ":
                file.write(e)

    def rewriteMD(self):
        emdList = self._emdList
        emd = []

        for k, d in emdList.items():
            data = k.split('/')  # split the key: 201911007/1
            line = "%s,%s,%s\n" % (data[0],data[1],d)
            emd.append(line)

        file = open("EMList.txt", "w")
        for e in emd:
            if e != " ":
                file.write(e)

        file.close()

    def generatePS(self,selectedMonth,month,empNum):
        eRecord = self._eList
        emRecord = self._emdList
        monthIndex = int(month.index(selectedMonth)) + 1
        try:
            salary = int(eRecord[empNum.get()]['Rate per day']) * int(emRecord[empNum.get() + '/' + str(monthIndex)])
            genPayslip = "\t\t\tABC COMPANY" + "\nPayslip of the Month:" + str(selectedMonth).upper() + "\nEmployee Number: " + empNum.get() + \
                         "\t\tName: " + eRecord[empNum.get()]['First name'] + " " + eRecord[empNum.get()]['Last name'] + \
                         "\nBirthdate: " + eRecord[empNum.get()]['Birthdate'] + \
                         "\nDepartment: " + eRecord[empNum.get()]['Department'] + "\t\t\tPosition: " + eRecord[empNum.get()]['Position'] + \
                         "\nRate per day: " + eRecord[empNum.get()]['Rate per day'] + \
                         "\nNo. of Days worked: " + emRecord[empNum.get() + '/' + str(monthIndex)] + \
                         "\n\nSalary for the month: {:,}".format(salary)
        except KeyError:
            return KeyError
        except ValueError:
            return ValueError

        with open(empNum.get()+ '-' + str(monthIndex) + ".txt", 'w') as genPS:
            genPS.write(genPayslip)

        genPS.close()
