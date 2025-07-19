eList = """201911007,Butt,James,Staff,Accounting,01-21-1993,475
201203008,Darakjy,Josephine,Staff,Sales and Marketing,08-04-1989,475
199710014,Venere,Art,Staff,Human Resources,750,10-11-1991,475
201612010,Paprocki,Lenna,Staff,Manufacturing,04-24-1988,475
201710017,Foller,Donnette,Staff,Admin,12-31-1996,475"""

eMDList = """201911007,1,31
201203008,1,24
199710014,1,30
201612010,1,31
201710017,1,22
201911007,2,28
201203008,2,21
199710014,2,27
201612010,2,28
201710017,2,24
201911007,3,31
201203008,3,28
199710014,3,30
201612010,3,31
201710017,3,28"""

def createFile():
    file = open('eList.txt','w')
    file.write(eList)
    file.close()

    file = open('EMList.txt', 'w')
    file.write(eMDList)
    file.close()

