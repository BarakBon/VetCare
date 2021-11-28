import sqlite3
from sqlite3 import *

#Gets a username and password and checks if it exists in the system - If so returns UserID
def Login_check (Name , Password):
    conn = sqlite3.connect('DataBase.db')
    c = conn.cursor()
    search = c.execute("SELECT * FROM Users WHERE UserName=? AND Password=?",(Name,Password))
    item =c.fetchone()
    if item is None:
        return False
    else:
        return item[0]
    conn.commit()
    conn.close()

def UserID_to_UserType (id):
    conn = sqlite3.connect('DataBase.db')
    c = conn.cursor()
    search = c.execute("SELECT * FROM Users WHERE UserID=?", (id))
    item = c.fetchone()
    if item is None:
        return False
    else:
        return item[1]
    conn.commit()
    conn.close()

ans=Login_check('OrB', 'OB26')
print (ans)
ans1=UserID_to_UserType('1')
print (ans1)

