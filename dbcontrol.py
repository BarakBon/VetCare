import sqlite3
from sqlite3 import *
import sqlite3 as lite
from sqlite3 import Error
conn = sqlite3.connect('DataBase.db')
c = conn.cursor()
#The function gets a username and checks if it exists and if it exists it returns its details
def Search (Name):
    conn = sqlite3.connect('DataBase.db')
    c = conn.cursor()
    search = c.execute("SELECT * FROM Users WHERE UserName=? ",(Name,))
    item =c.fetchone()
    if item is None:
        return False
    else:
        t=(item[0],item[3], item[4],item[5],item[6],item[7],item[8])
        return t

    conn.commit()
    conn.close()

S= Search('ZapaA')
print (S)
