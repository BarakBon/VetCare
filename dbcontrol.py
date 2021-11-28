import sqlite3


conn = sqlite3.connect("DataBase.db")
c = conn.cursor()
def newcustomer(userName,Password,firstName,lastName,Address,phoneNumber,mailAddress,userType):
#A function that builds a new user
    c.execute("INSERT INTO `Users` ('UserName','Password', 'FirstName', 'LastName', 'Address', 'PhoneNumber', 'MailAddress', 'UserType') VALUES (?,?,?,?,?,?,?,?);",(userName,Password,firstName,lastName,Address,phoneNumber,mailAddress,userType))

def printUser(userName):
#A function that prints the user information you requested
    c.execute('SELECT * FROM `Users` WHERE UserName ="' + userName + '" ' )
    for row in c:
        print(row)

def newAnimal(userID,Type,animalName,importantInfo):
#A function that creates an animal for the user according to ID
    c.execute("INSERT INTO `Animals` ('userID','Type','animalName','importantInfo') VALUES (?,?,?,?);",(userID,Type,animalName,importantInfo))

def printanimals(UserID):
#A function that prints all the animals of the user according to ID
    c.execute('SELECT * FROM `Animals` WHERE UserID ="' + UserID + '" ' )
    for row in c:
        print(row)

print("plz enter your customer details:")
UserName=input("User Name")
Password=input("Password,Letters and Numbers")
FirstName=input("First Name")
LastName=input("Last Name")
Address=input("Hometown")
PhoneNumber=input("Phone Number")
MailAddress=input("Mail Address")
UserType=input("User Type")

newcustomer(UserName,Password,FirstName,LastName,Address,PhoneNumber,MailAddress, UserType)
printUser(UserName)
print("plz enter the animal details:")
UserID=input("customer User ID")
Type= input("User Type of animal")
AnimalName=input("Animal Name")
ImportantInfo=input("Important Info about the animal")
newAnimal(UserID,Type,AnimalName,ImportantInfo)
printanimals(UserID)

conn.commit()
conn.close()