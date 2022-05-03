
#import passwordProject
"""
verifyingPass(password)
    -returns true or false

forgetPassword(username, ans1, ans2)
    -ask security question
    -call createPassword
    -sets the new password



"""


def home(user):
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
    accountsPath = "accounts.txt"

    oldPassword = input("Enter your old password")

    with open(accountsPath, 'r') as file:
        data = file.readlines()

    userNameLocation = 0
    for line in data:
        if line == username:
            break
        userNameLocation += 1
    if(oldPassword != data[userNameLocation + 1]):
        print("Old password is wrong!")
        return False
    newPassword = input("Enter the new password")
    #Check Requirements
    data[userNameLocation + 1] = newPassword # Add Encryption later
    with open(accountsPath, 'w') as file:
        files.writelines(data)
    return True


username = "test1"
#addData(username, "app2", "app2User", "app2PW")
home(username)
