import homepage


def userNameIndex(username):
    with open("Accounts.txt", 'r') as file:
        data = file.readlines()
    usernameLocation = 0

    for line in data:
        if line.strip() == username:
            found = True
            break
        usernameLocation += 1
    return usernameLocation

#When Given a username associated with an account
#Register a new password into Accounts.txt
def createPassword(username):

    stringOfalph = "abcdefghijklmnopqrstuvwxyz".upper()
    stringOfSpecial = "!@#$%^&*()"
    stringOfNum = "0123456789"

    boolForNum = False
    boolForCap = False

    #Run Through a continuous loop until a valid password is created
    #Must have num, upperChar, and SpecialChar
    #Min Length 7
    while(boolForCap != True or boolForNum != True):
        password = input("Enter a password(Min Length 7, one Number, one Capital): ")
        while (len(password) < 7):
            password = input("Password not long enough, try again: ")

        for i in range(len(password)):
            for j in range(len(stringOfalph)):
                if (password[i] == stringOfalph[j]):
                    boolForCap = True


        for i in range(len(password)):
            for j in range(len(stringOfNum)):
                if (password[i] == stringOfNum[j]):
                    boolForNum = True

        if (boolForNum != True):
            print("No number Found")
        if(boolForCap != True):
            print("No capital Found")


    #Password should be verified now
    password = password + "\n"

    #Find location of username, directly below should be the password
    with open("Accounts.txt", 'r') as file:
        data = file.readlines()
    usernameLocation = userNameIndex(username)

    #If new user, add a new line
    if usernameLocation + 1 > len(data) - 1:
        data.append(password)
    else:
        data[usernameLocation + 1] = password

    #Write data back to file
    with open("Accounts.txt", 'w') as file:
        file.writelines(data)
        


def createAccount():
    #create username
    username = input("Enter your username")
    username = username + "\n"
    fileOut = open("Accounts.txt", 'a')
    fileOut.write(username)
    fileOut.close()

    createPassword(username.strip())

    SecurityQuestionAnswers(username.strip())

    userData = username.strip() + "Data.txt"
    tmp = open(userData,'w')
    tmp.close()


def SecurityQuestionAnswers(username):
    A1 = input("What is your homecountry? ")
    A2 = input("What is your favorite hobby? ")
    x = A1 + '\n'
    x2 = A2 + '\n'
    
    filePath = username + "Security.txt"
    fileOut = open(filePath, 'w')
    
    fileOut.write(x)
    fileOut.write(x2)
    fileOut.close()

    

def forgotPassword(username):
    #ask for verifying security questions
    ans1 = input("What is your homecountry? ")
    ans2 = input("What is your favorite hobby? ")
    
    x = username + "Security.txt"
    fileIn = open(x, 'r')
    q1 = fileIn.readline().strip()
    q2 = fileIn.readline().strip()
    fileIn.close()
    
    if(q1  == ans1 and q2 == ans2):
        createPassword(username)
    else:
        print("Security question answers are wrong")

def Login():
    usrInput = 0
    while usrInput != 4:
        print("LOGIN PAGE")
        print("1) Create Account")
        print("2) Forgot Password")
        print("3) Login")
        print("4) Exit")

        usrInput = int(input())

        if(usrInput == 1):
            createAccount()
        elif(usrInput == 2):
            input2 = input("What was the username: ")
            forgotPassword(input2)
        elif(usrInput == 3):
            inputUsername = input("Username: ")
            inputPassword = input("Password: ")
            
            with open("Accounts.txt", 'r') as file:
                data = file.readlines()
            usernameLocation = userNameIndex(inputUsername)

            if usernameLocation > len(data) - 1:
                print("failed login attempt")
            else:
                if inputPassword == data[usernameLocation + 1].strip():
                    print("logged in!")
                    homepage.home(inputUsername)
                else:
                    print("failed login attempt")

Login()


