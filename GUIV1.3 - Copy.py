#Ecryption GUI Version 1.3 
#Last Edit: 5/4/2022
from tkinter import *
from tkinter import messagebox, ttk

import os
import homepage
import main
relativePath = os.path.join(os.path.dirname(__file__), 'users')

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

def createPassword(username,passwordUser):

    stringOfalph = "abcdefghijklmnopqrstuvwxyz".upper()
    stringOfSpecial = "!@#$%^&*()"
    stringOfNum = "0123456789"

    boolForNum = False
    boolForSpec = False
    boolForCap = False

    #Run Through a continuous loop until a valid password is created
    #Must have num, upperChar, and SpecialChar
    #Min Length 7
    password = passwordUser
    for i in range(len(password)):
        for j in range(len(stringOfalph)):
            if (password[i] == stringOfalph[j]):
                boolForCap = True

    for i in range(len(password)):
        for j in range(len(stringOfSpecial)):
            if (password[i] == stringOfSpecial[j]):
                boolForSpec = True

    for i in range(len(password)):
        for j in range(len(stringOfNum)):
            if (password[i] == stringOfNum[j]):
                boolForNum = True

    if len(password) < 7:
        return False
    if boolForCap != True and boolForNum != True and boolForSpec != True:
        return False


    account_file = open("Accounts.txt", "a")
    account_file.write(username+"\n")
    account_file.close()

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

    return True

#Creates popup window telling user their password is wrong
def newPasswordNotValid():
    global password_error_screen
    password_error_screen = Toplevel(screen)
    password_error_screen.title("Error")
    password_error_screen.geometry("300x100")
    Label(password_error_screen, text= "One of the following was no met:\nLength less than 7\nNo Capital Letter\nNo Number\nNo Special Character").pack()
    Button(password_error_screen, text= "OK", command=delete_pass_error_window).pack()

#Creates Accounts.txt if it does not exist withing directory and stores new account info
#Also creates Security text file under the new user's name and displays success message when completed
def register_user():
    username_info = username.get()
    password_info = password.get()
    color_info = color.get()
    restaurant_info = restaurant.get()

    tmp = createPassword(username_info,password_info)
    if(tmp != True):
        newPasswordNotValid()
    else:
        main.SecurityQuestionAnswers(username_info, color_info, restaurant_info)
        #closes registration window and displays success message
        registration_screen.destroy()
        messagebox.showinfo(title="Success!", message="Account successfully created!")

#Account Creation Page
#User is prompted to enter a username, password, favorite color(Security question 1), and favorite restaurant(Security question 2)
def register():
    global registration_screen
    registration_screen = Toplevel(screen)
    registration_screen.title("Create Account")
    registration_screen.geometry("400x350")

    global username, username_entry, password, password_entry, color, color_entry, restaurant, restaurant_entry
    username = StringVar()
    password = StringVar()
    color = StringVar()
    restaurant = StringVar()

    Label(registration_screen, text= "Please enter your details below.").pack()
    Label(registration_screen, text= "").pack()
    Label(registration_screen, text= "Username").pack()
    username_entry = Entry(registration_screen, textvariable= username).pack()
    Label(registration_screen, text= "Password").pack()
    password_entry = Entry(registration_screen, textvariable= password).pack()
    Label(registration_screen, text= "").pack()
    Label(registration_screen, text= "Security Questions").pack()
    Label(registration_screen, text= "What is your favorite color?").pack()
    color_entry = Entry(registration_screen, textvariable= color).pack()
    Label(registration_screen, text= "What is your favorite restaurant?").pack()
    restaurant_entry = Entry(registration_screen, textvariable= restaurant).pack()
    Label(registration_screen, text= "").pack()
    Button(registration_screen, text = "Register", width= 10, height=1, command=register_user).pack()
def end_program():
    screen.destroy()

#Logs the current user out of the program and returns to the main screen
#CURRENTLY UNDEFINED
def log_out():
    print()

#Enters the main user dashboard after a successful login process
def enter_user_portal():
    user_portal = Toplevel(screen)
    user_portal.title(username_check + "'s Dashboard")
    user_portal.geometry("400x400")
    login_screen.destroy()
    #Will try figure out how to hide main screen as well

    #Display user options
    Button(user_portal, text = "View My Passwords", width= 25, height=1, command=display_info).pack()
    Button(user_portal, text = "Log Out", width= 25, height=1, command=log_out).pack()
    Button(user_portal, text = "Close Program", width= 25, height=1, command=end_program).pack()
#Displays new window with current user's password data
def display_info():
    global user_information_screen, entry_counter
    user_information_screen = Toplevel(screen)
    user_information_screen.title("Your Data")
    user_information_screen.geometry("800x800")
    info_tree = ttk.Treeview(user_information_screen)
    entry_counter = 0
    #Define columns
    info_tree["columns"] = ("Application", "Username", "Password")
    #Format columns
    info_tree.column("#0", width=0, minwidth=25)
    info_tree.column("Application", anchor=W, width=200, minwidth=25)
    info_tree.column("Username", anchor=W, width=200, minwidth=25)
    info_tree.column("Password", anchor=W, width=200, minwidth=25)
    #Headings
    info_tree.heading("#0", text="", anchor=W)
    info_tree.heading("Application", text="Application", anchor=W)
    info_tree.heading("Username", text="Username", anchor=W)
    info_tree.heading("Password", text="Password", anchor=W)

    #getData retrieves a list with contents from user data file
    #getDataLists interprets the data to yield 3 seprate lists
    applicationsList, usernamesList, passwordsList = homepage.getDataLists( homepage.getData(username_check) )

    #Group information in tuples to pass for ttk.Treeview
    userDatas = []
    for appItem, userItem, passwordItem in zip(applicationsList, usernamesList, passwordsList):
        userDatas.append((appItem, userItem, passwordItem))
    for userData in userDatas:
        info_tree.insert(parent="", index="end", iid=entry_counter, text="", values= userData)
        entry_counter += 1
    
    info_tree.pack()
    
    '''Note: add database interaction for below functions'''
    #adds data entry
    def add_record():
        global entry_counter
        info_tree.insert(parent="", index="end", iid=entry_counter, text="", values=(app_box.get(), user_box.get(), pass_box.get()))
        homepage.addData(username_check, app_box.get(), user_box.get(), pass_box.get())
        app_box.delete(0, END)
        user_box.delete(0, END)
        pass_box.delete(0, END)
        entry_counter += 1
        
    #removes all data entries
    def clear_records():
        for record in info_tree.get_children():
            info_tree.delete(record)
        filePath = username_check + "Data.txt"
        filePath = os.path.join(relativePath, filePath)

        with open(filePath, 'a') as file:
            file.truncate(0)
        entry_counter = 0
            
    #removes highlighted data entry
    def remove_selected():
        homepage.removeData(username_check, info_tree.selection())
        for record in info_tree.selection():
            info_tree.delete(record)
            entry_counter -= 1
        

        
    #Add Entry Frame
    add_frame = Frame(user_information_screen)
    add_frame.pack(pady=20)
    #Entry Box labels
    app_label = Label(add_frame, text="Application")
    app_label.grid(row=0, column=0)

    user_label = Label(add_frame, text="Username")
    user_label.grid(row=0, column=1)

    pass_label = Label(add_frame, text="Password")
    pass_label.grid(row=0, column=2)

    #Entry Boxes
    app_box = Entry(add_frame)
    app_box.grid(row=1, column=0)

    user_box = Entry(add_frame)
    user_box.grid(row=1, column=1)

    pass_box = Entry(add_frame)
    pass_box.grid(row=1, column=2)

    #Buttons
    add_record = Button(user_information_screen, text="Add Record", command=add_record)
    add_record.pack(pady=20)
    clear_records = Button(user_information_screen, text="Clear All Data", command=clear_records)
    clear_records.pack(pady=10)
    remove_selected = Button(user_information_screen, text="Remove Selected", command=remove_selected)
    remove_selected.pack(pady=10)

#Deletes username error popup
def delete_user_error_window():
    username_error_screen.destroy()

#Creates popup window telling user their username is not registered
def user_not_found():
    global username_error_screen
    username_error_screen = Toplevel(screen)
    username_error_screen.title("Error")
    username_error_screen.geometry("300x100")
    Label(username_error_screen, text= "Username not in records. Try Again.").pack()
    Button(username_error_screen, text= "OK", command=delete_user_error_window).pack()

#Deletes password error popup
def delete_pass_error_window():
    password_error_screen.destroy()

#Creates popup window telling user their password is wrong
def password_not_recognized():
    global password_error_screen
    password_error_screen = Toplevel(screen)
    password_error_screen.title("Error")
    password_error_screen.geometry("300x100")
    Label(password_error_screen, text= "Password does not match records. Try Again.").pack()
    Button(password_error_screen, text= "OK", command=delete_pass_error_window).pack()

#This function acts as the login verification process
#The account file is searched for credentials and the user is given a popup message if something goes wrong
def verify_login():
    global username_check
    username_check = verify_user.get()
    password_check = verify_password.get()
    try:
        with open("Accounts.txt") as account_file:
            account_list = account_file.readlines()             #places account pairs into list in order to verify information
            account_list = [x.strip() for x in account_list]    #removes newline chars from names so info can be read properly
            if username_check in account_list:
                for i in range(len(account_list)):                  #searches Account file for entered info. Enters user portal if successful. Displays error messages if unsuccessful.
                    if account_list[i] == username_check:
                        if account_list[i+1] == password_check:
                            enter_user_portal()
                        else:
                            password_not_recognized()
            else:
                user_not_found()
    except FileNotFoundError:
        messagebox.showinfo(title="Uh oh!", message="This file does not contain any account information. Please ensure that an account has been previously created in this directory.")

#Will take user to a screen where they will enter their username
#Upon username verification they will enter their security questions in a pop up window
#Upon verification of the questions they will be told their password
#CURRENTLY UNDEFINED
def recover_password():
    print() #Placeholder

#Login Info Page
#Displays Username and Password fields alone with Log In and Forgot Password buttons
def login():
    global login_screen, verify_user, verify_password, username_login_attempt, password_login_attempt
    login_screen = Toplevel(screen)
    login_screen.title("Log In Window")
    login_screen.geometry("400x350")

    verify_user = StringVar()
    verify_password = StringVar()

    Label(login_screen, text= "Please enter your details to log in.").pack()
    Label(login_screen, text= "").pack()
    Label(login_screen, text= "Username").pack()
    username_login_attempt = Entry(login_screen, textvariable= verify_user).pack()
    Label(login_screen, text= "").pack()
    Label(login_screen, text= "Password").pack()
    password_login_attempt = Entry(login_screen, textvariable= verify_password).pack()
    Label(login_screen, text= "").pack()
    Button(login_screen, text = "Log In", width= 10, height=1, command=verify_login).pack()
    Button(login_screen, text = "Forgot Password?", width= 15, height=1, command=recover_password).pack()

#Main Program Window with Login and Register buttons
def main_window():
    global screen
    
    if not os.path.exists(relativePath):
        os.makedirs(relativePath)
    
    screen = Tk()
    screen.geometry("400x350")
    screen.title("Password Management")
    Label(text="Welcome to Password Management V1.3!", width="300", height="2").pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Create Account", height="2", width="30", command=register).pack()

    screen.mainloop()

main_window()
