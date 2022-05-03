#Function for user login
def verifyingPass(password):
    #ask user to renter the password created
    #use this function in create password
    reenter = input("re-enter the password:")
    return (reenter == password)

def createPassword(username):
    fileOut = open("Accounts.txt", 'a')
    stringOfalph = "abcdefghijklmnopqrstuvwxyz"
    stringOfSpecial = "!@#$%^&*()"
    stringOfNum = "0123456789"

    boolForNum = False
    boolForCap = False
    boolForSpecial = False

    while(boolForSpecial != True and boolForCap != True and boolForNum != True):
        password = input("Enter a password(Min Length 7, one Number, one Capital and One special Character): ")
        while (len(password) < 7):
            password = input("Password not long enough, try again: ")

        for i in range(len(password)):
            for j in range(len(stringOfalph)):
                if (password[i] == stringOfalph[j]):
                    boolForCap = True

        for i in range(len(password)):
            for j in range(len(stringOfSpecial)):
                if (password[i] == stringOfSpecial[j]):
                    boolForSpecial = True

        for i in range(len(password)):
            for j in range(len(stringOfNum)):
                if (password[i] == stringOfNum[j]):
                    boolForNum = True

        if (boolForNum != True):
            print("No number Found")
        if(boolForCap != True):
            print("No capital Found")
        if (boolForSpecial != True):
            print("No Special Found")
    #identify location
    fileOut.write(password)

    #calls verifying password

def createAccount():
    #create username
    username = input("Enter your username")
    username = username + "\n"
    fileOut = open("Accounts.txt", 'a')
    fileOut.write(username)
    fileOut.close()
    #calls create password
    #calls verifying password
    #create Security answers
    #writes the username and password into a file
    #create dictionary zip username and password together
def createSecurityAnswer(username):
    A1 = input("What is your homecountry? ")
    A2 = input("What is your favorite hobby? ")
    filePath = username + "Securityans.txt"
    fileOut = open(filePath, 'a')
    x = A1 + '\n'
    x2 = A2 + '\n'

    fileOut.write(x)
    fileOut.write(x2)
    fileOut.close()
def Login():
    #Enter User name and password 3 tries
    print("Logged in successfully welcome")

def changePassword():
    #calls create Password using username as key

def forgotPassword(username):
    #ask for verifying security questions
    ans1 = input("What is your homecountry? ")
    ans2 = input("What is your favorite hobby? ")
    x = username + "security.txt"
    fileIn = open(x, 'r')
    q1 = fileIn.readline()
    q2 = fileIn.readline()
    fileIn.close()
    if(q1  == ans1 and q2 == ans2):
        #call createPassword
    else:
        print("Security question answers are wrong")

#STOP HERE!

def login(d):
    #boolean value for when person successfully logs in
    unlock = False
    #Loop to continue to find username
    while True:
        username = input("Enter a username: ")
        if username in d.keys() :
            #Counter to increment count for tries
            counter = 0
            # two conditions one for checking pass and username correct and counter
            while counter < 3 and not unlock:
                password = input("Enter a password: ")
                if password == d[username]:
                    unlock = True
                else:
                    counter += 1
                    print("Retry password")
            if unlock == True:
                print("Successfully Logged in")
                break

    print("Admin is", username)
    yOrN = input("Do you want to add user yes or no: ")
    if yOrN == 'yes':
        print("Old Users: ", d)
        addUser(d)
        print("New dictionary: ", d)
    yOrN2 = input("Do you want to change password yes or no: ")

    if yOrN2 == 'yes':
        print("Old Passwords: ", d)
        changePass(d)
        print("New dictionary: ", d)

def changePass(d):
    #entering a username key to access password
    username = input("Enter username for password change: ")
    #changing the password for the specific username
    d[username] = input("New password: ")

def addUser(d):
    #entering a new username and new password
    newUser = input("Enter new username: ")
    newPassword = input("Enter new password: ")
    #adding it into the dictionary
    d.update({newUser: newPassword})

def main():
    stringOfalph = "abcdefghijklmnopqrstuvwxyz"
    stringOfSpecial = "!@#$%^&*()"

    # creating set of usernames
    setOfNames = {"Alex", "Betty", "Kim"}

    listOfPass = []
    print("Create a username and password, enter list of password ")

    for i in range(len(setOfNames)):
        password = input("Enter a password(Min Length 15, one Capital and One special Character): ")

        if(len(password) < 7):
            print("Try again")
        for i in range(len(password)):
            for j in range(len(stringOfalph)):
                if(password[i] == stringOfalph[j]):
                    return True
        for i in range(len(password)):
            for j in range(len(stringOfSpecial)):
                if (password[i] == stringOfSpecial[j]):
                    return True

        listOfPass.append(password)
    #create the dictonary
    users = dict(zip(list(setOfNames), listOfPass))

    print(users)
    login(users)


main()
