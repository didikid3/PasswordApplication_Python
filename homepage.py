import os
relativePath = os.path.join(os.path.dirname(__file__), 'users')

#Given the list of user data
#Return a user's data formatted into 3 lists
def getDataLists(data):
    application = []
    usernames = []
    passwords = []
    count = 0
    for line in data:
        if count == 0:
            application.append(line.strip())
            count += 1
        elif count == 1:
            usernames.append(line.strip())
            count += 1
        else:
            passwords.append(line.strip())
            count = 0

    return application,usernames,passwords


def home(user):
    userInput = ""
    while userInput != 3:

        dataList = getData(user)

        count = 0
        tmpString = ""
        print("APPLICATION\t\tUsername\t\tPassword")
        for line in dataList:
            if count != 2:
                tmpString += line.strip() + "\t\t"
                count += 1
            else:
                tmpString += line.strip()
                print(tmpString)
                tmpString = ""
                count = 0

        
        print("1) Add Data")
        print("2) Change Password")
        print("3) Log Out")
        userInput = int(input())

        if userInput == 1:
            application = input("What App is this for?")
            userName = input("The username for " + application + ": ")
            password = input("The password for " + application + ": ")
            addData(user, application, userName, password)
        elif userInput == 2:
            changePassword(user)
        
#Returns the array containing user's data
def getData(user):
    filePath = user + "Data.txt"
    filePath = os.path.join(relativePath, filePath)
    with open(filePath, 'r') as file:
        data = file.readlines()
    return data

#Given the user, and the new details to add
#Insert into user's file the new data
def addData(user, app, userName, password):
    filePath = user + "Data.txt"
    filePath = os.path.join(relativePath, filePath)

    fileOut = open(filePath, 'a')
    text = app +'\n' + userName + '\n' + password + '\n'
    fileOut.write(text)
    fileOut.close()

#Given specific index locations of data
#Remove the data associate with the index
def removeData(user, indexes):
    removeList = []
    for ind in indexes:
        removeList.append(int(ind)*3)
        removeList.append(int(ind)*3 + 1)
        removeList.append(int(ind)*3 + 2)

    filePath = user + "Data.txt"
    filePath = os.path.join(relativePath, filePath)

    with open(filePath, 'r') as file:
        data = file.readlines()

    with open(filePath, 'w') as file:
        for index, line in enumerate(data):
            if index not in removeList:
                file.write(line)

#Old ChangePassword
#Overwritten version in GUI file
#May be used if want to run text based
def changePassword(username):
    accountsPath = "Accounts.txt"

    oldPassword = input("Enter your old password")

    with open(accountsPath, 'r') as file:
        data = file.readlines()

    userNameLocation = 0
    for line in data:
        if line.strip() == username:
            break
        userNameLocation += 1
    if oldPassword != data[userNameLocation + 1].strip():
        print("Old password is wrong!")
        return False
    newPassword = input("Enter the new password")
    #Check Requirements
    data[userNameLocation + 1] = newPassword # Add Encryption later
    with open(accountsPath, 'w') as file:
        files.writelines(data)
    return True

