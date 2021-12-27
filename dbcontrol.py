import sqlite3
conn = sqlite3.connect("DataBase.db")
c = conn.cursor()
import re

def newcustomer(userName,Password,firstName,lastName,Address,phoneNumber,mailAddress,userType):
    # A function that checks if the username already existed, if not builds a new user
    search = c.execute("SELECT * FROM Users WHERE UserName=?", (userName,))
    item = c.fetchone()
    if item:
        return -1
    #checking the phone number
    if ((len(phoneNumber)!=10) or (phoneNumber.isdecimal()!=True)):
        return -2
    #checking username and password
    if ((len(userName)<3) or (userName.isalnum() != True) or (len(Password)<3)):
        return -2
    #checking address , first and last name
    if ((firstName.isalpha()!=True) or (lastName.isalpha()!=True) or (Address.isalpha()!=True)):
        return -2
    match = re.search(r'[\w.-]+@[\w.-]+.\w+', mailAddress)
    if not match:
        return -2
    else:
        c.execute("INSERT INTO `Users` ('UserName','Password', 'FirstName', 'LastName', 'Address', 'PhoneNumber', 'MailAddress', 'UserType') VALUES (?,?,?,?,?,?,?,?);",(userName,Password,firstName,lastName,Address,phoneNumber,mailAddress,userType))
        conn.commit()

def newAnimal(userID,Type,animalName,importantInfo):
    # A function that creates an animal for the user according to ID
    c.execute("INSERT INTO `Animals` ('userID','Type','animalName','importantInfo') VALUES (?,?,?,?);",(userID,Type,animalName,importantInfo))

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
    t=()
    c.execute("SELECT * FROM Appointments WHERE AppointmentDate=? ", (str(Date),))
    item = c.fetchall()
    if not item:
        Date_Check(Date)
        return 'all appointments are free'
    else:
        for item in item:
            if item[1] != None:
                t += ((item[2],item[1]),)
        return t
    conn.commit()

#Shows the free hours on the date
def Show_appointment(Date):
    t=[]
    c.execute("SELECT * FROM Appointments WHERE AppointmentDate=? ", (str(Date),))
    item = c.fetchall()
    if item == []:
        return Date_Check(Date)

    else:
        for item in item:
            if not item[1] :
                t += [item[2]]
        return t
    conn.commit()


conn.commit()
# conn.close()

#A function that gets a UserID and returns the username
def UserName(ID):
    c.execute("SELECT * FROM Users WHERE UserID=?",(ID,))
    item=c.fetchone()
    if item is None:
            return -1
    else:
        t=[item[3],item[4]]
        return t

#the function get userID and Animal name and returns the important information
def get_important_note(userID,animalName):
    c.execute("SELECT * FROM Animals WHERE UserID=? AND AnimalName=?", (userID, animalName))
    item = c.fetchone()
    if item is None:
        return -1
    else:
        return item[3]


#Gets date and time and adds queue
def Queue_registration(AnimalName,UserID,Date,Time):
    c.execute("UPDATE Appointments SET UserID=?,AnimalName=? WHERE AppointmentDate=? AND AppointmentTime=?",(UserID,AnimalName,Date,Time))
    conn.commit()

#Sets the important details about the animal
def set_important_note(userID,animalName,importantNote):
    c.execute("UPDATE Animals SET ImportantInfo=? WHERE UserID=? AND AnimalName=?",(importantNote, userID, animalName))
    conn.commit()

#Receives documentation and updates an existing queue if no new queue is created with the data
def set_treatments(ID,Name,Time,Date,Document):
    c.execute("UPDATE Treatments SET TreatmentDocument=? WHERE UserID=? AND AnimalName=? AND AppointmentTime=? AND AppointmentDate=?",(Document,ID,Name,Time,Date))
    c.execute("SELECT * FROM Treatments  WHERE UserID=? AND AnimalName=?AND AppointmentTime=? AND AppointmentDate=?", (ID, Name,Time,Date))
    item=c.fetchone()
    if item is None:
       c.execute("INSERT INTO Treatments ('userID','AnimalName','AppointmentTime','AppointmentDate','TreatmentDocument') VALUES (?,?,?,?,?);",(ID,Name,Time,Date,Document))
    conn.commit()

#Receives user ID and animal name , and returns the Animal details
def animal_details(ID, animalName):
    c.execute("SELECT * FROM Animals WHERE UserID=? AND AnimalName=?", (ID, animalName))
    item = c.fetchone()
    if item is None:
        return -1
    else:
        return (item[1], item[2],item[3])
#