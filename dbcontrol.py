import sqlite3
conn = sqlite3.connect("DataBase.db")
c = conn.cursor()

def newcustomer(userName,Password,firstName,lastName,Address,phoneNumber,mailAddress,userType):
    # A function that checks if the username already existed, if not builds a new user
    search = c.execute("SELECT * FROM Users WHERE UserName=?", (userName,))
    item = c.fetchone()
    if item:
        return -1
    c.execute("INSERT INTO `Users` ('UserName','Password', 'FirstName', 'LastName', 'Address', 'PhoneNumber', 'MailAddress', 'UserType') VALUES (?,?,?,?,?,?,?,?);",(userName,Password,firstName,lastName,Address,phoneNumber,mailAddress,userType))
    conn.commit()

def printUser(userName):
    # A function that prints the user information you requested
    c.execute('SELECT * FROM `Users` WHERE UserName ="' + userName + '" ' )
    for row in c:
        print(row)

def newAnimal(userID,Type,animalName,importantInfo):
    # A function that creates an animal for the user according to ID
    c.execute("INSERT INTO `Animals` ('userID','Type','animalName','importantInfo') VALUES (?,?,?,?);",(userID,Type,animalName,importantInfo))

def printanimals(UserID):
    # A function that prints all the animals of the user according to ID
    c.execute('SELECT * FROM `Animals` WHERE UserID ="' + UserID + '" ' )
    for row in c:
        print(row)

# print("plz enter your customer details:")
# UserName=input("User Name")
# Password=input("Password,Letters and Numbers")
# FirstName=input("First Name")
# LastName=input("Last Name")
# Address=input("Hometown")
# PhoneNumber=input("Phone Number")
# MailAddress=input("Mail Address")
# UserType=input("User Type")
#
# newcustomer(UserName,Password,FirstName,LastName,Address,PhoneNumber,MailAddress, UserType)
# printUser(UserName)
# print("plz enter the animal details:")
# UserID=input("customer User ID")
# Type= input("User Type of animal")
# AnimalName=input("Animal Name")
# ImportantInfo=input("Important Info about the animal")
# newAnimal(UserID,Type,AnimalName,ImportantInfo)
# printanimals(UserID)

# Gets a username and password , and checks if it exists in the system - If so returns UserID
def Login_check (Name , Password):
    search = c.execute("SELECT * FROM Users WHERE UserName=? AND Password=?",(Name,Password))
    item =c.fetchone()
    if item is None:
        return False
    else:
        # The index of the UserID
        return item[0]

#Gets a user ID  and checks if it exists in the system - If so returns the user first name
def UserID_to_First_Name (id):
    search = c.execute("SELECT * FROM Users WHERE UserID=?", (str(id)))
    item = c.fetchone()
    if item is None:
        return False
    else:
        #The index of the user first name
        return item[3]

#Gets a user ID  and checks if it exists in the system - If so returns UserType
def UserID_to_UserType (id):
    search = c.execute("SELECT * FROM Users WHERE UserID=?", (str(id)))
    item = c.fetchone()
    if item is None:
        return False
    else:
        # The index of the UserType
        return item[8]
      

#The function gets a username and checks if it exists and if it exists it returns its details
def Search (Name):
    search = c.execute("SELECT * FROM Users WHERE UserName=? ",(Name,))
    item =c.fetchone()
    if item is None:
        return False
    else:
        t=(item[0],item[3], item[4],item[5],item[6],item[7],item[8])
        return t

def AnimalName(ID):
    t=[]
    c.execute("SELECT * FROM Animals WHERE UserID=? ", (ID,))
    item = c.fetchall()
    if item:
     for item in item:
      t+=[item[2]]
     return t
    else:
        return -1
conn.commit()
# conn.close()



t=AnimalName(5)
print(t)
