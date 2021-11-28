import sqlite3
from sqlite3 import *

conn = sqlite3.connect('DataBase.db')
c = conn.cursor()

#Gets a username and password , and checks if it exists in the system - If so returns UserID
def Login_check (Name , Password):
    search = c.execute("SELECT * FROM Users WHERE UserName=? AND Password=?",(Name,Password))
    item =c.fetchone()
    if item is None:
        return False
    else:
        # The index of the UserID
        return item[0]

#Gets a user ID  and checks if it exists in the system - If so returns UserName
def UserID_to_UserName (id):
    search = c.execute("SELECT * FROM Users WHERE UserID=?", (id))
    item = c.fetchone()
    if item is None:
        return False
    else:
        #The index of the UserName
        return item[1]

#Gets a user ID  and checks if it exists in the system - If so returns UserType
def UserID_to_UserType (id):
    search = c.execute("SELECT * FROM Users WHERE UserID=?", (id))
    item = c.fetchone()
    if item is None:
        return False
    else:
        # The index of the UserType
        return item[8]



ans=Login_check('OrB', 'OB26')
print (ans)
ans1=UserID_to_UserName('6')
print (ans1)
ans2=UserID_to_UserType('2')
print (ans2)

conn.commit()
conn.close()