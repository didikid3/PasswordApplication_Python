
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
        

def getData(user):
    filePath = user + "Data.txt"
    with open(filePath, 'r') as file:
        data = file.readlines()
    return data

def addData(user, app, userName, password):
    filePath = user + "Data.txt"

    fileOut = open(filePath, 'a')
    text = app +'\n' + userName + '\n' + password + '\n'
    fileOut.write(text)
    fileOut.close()


    
def changePassword(username):
    securityPath = username + "Security.txt"
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

