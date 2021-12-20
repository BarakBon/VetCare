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
#The function gets a UserID and checks if it is found returns the names of the animals
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

#Checks if a date exists or not,If so return the existing hours, if not create hours in the system and returns them
def Date_Check(Date):
    t = []
    c.execute("SELECT * FROM Appointments WHERE AppointmentDate=:dateToCheck", {"dateToCheck": str(Date)})
    item = c.fetchall()
    if not item:
        Time = 8
        while Time<=19:
            c.execute("INSERT INTO `Appointments` ('AppointmentDate','AppointmentTime') VALUES (:newDate, :newTime);", {"newDate": str(Date), "newTime": str(Time)})
            conn.commit()
            Time+=1
            for item in item:
                t += [item[2]]
        return t
    else:
        for item in item:
            t += [item[2]]
        return t
    conn.commit()


#Returns all busy appointments on a date
def retu_appoin(Date):
    t=[]
    c.execute("SELECT * FROM Appointments WHERE AppointmentDate=? ", (str(Date),))
    item = c.fetchall()
    if not item:
        Date_Check(Date)
        return 'all appointments are free'
    else:
        print("busy appointments of the date ", Date)
        for item in item:
            if item[1] != None:
                t += [item[1],item[2]]
        return t
    conn.commit()

#Shows the free hours on the date
def Show_appointment(Date):
    t=[]
    c.execute("SELECT * FROM Appointments WHERE AppointmentDate=? ", (str(Date),))
    item = c.fetchall()
    if item == []:
        print("Appointments available for ", Date)
        return Date_Check(Date)

    else:
        print("Appointments available for ", Date)
        for item in item:
            if not item[1] :
                t += [item[2]]
        return t
    conn.commit()


conn.commit()
# conn.close()

#print(Show_appointment('05/10/21'))
#print_appoin('05/10/21')
#print(Show_appointment_today('30/10/21'))
#t=AnimalName(5)
#print(t)

#A function that gets a UserID and returns the username
def UserName(ID):
    c.execute("SELECT * FROM Users WHERE UserID=?",(ID,))
    item=c.fetchone()
    if item is None:
            return -1
    else:
        t=[item[3],item[4]]
        return t


#z=UserName(5)
#print(z)
