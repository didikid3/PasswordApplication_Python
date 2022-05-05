#Ecryption GUI Version 1.3 
#Last Edit: 5/4/2022
from tkinter import *
from tkinter import messagebox, ttk

#Creates Accounts.txt if it does not exist withing directory and stores new account info
#Also creates Security text file under the new user's name and displays success message when completed
def register_user():
    username_info = username.get()
    password_info = password.get()
    color_info = color.get()
    restaurant_info = restaurant.get()

    account_file = open("Accounts.txt", "w")
    account_file.write(username_info+"\n")
    account_file.write(password_info+"\n")
    account_file.close()

    security_file = open(username_info+"Security.txt", "w")
    security_file.write(color_info+"\n")
    security_file.write(restaurant_info+"\n")
    security_file.close()

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
    #Populate Treeview
    info_tree.insert(parent="", index="end", iid=entry_counter, text="", values=("Work Computer", "John", "Python")) #filler data
    info_tree.pack()
    
    '''Note: add database interaction for below functions'''
    #adds data entry
    def add_record():
        global entry_counter
        entry_counter += 1      #adds counter first right now because of filler data. will change once the treeview reads from data text file
        info_tree.insert(parent="", index="end", iid=entry_counter, text="", values=(app_box.get(), user_box.get(), pass_box.get()))
        app_box.delete(0, END)
        user_box.delete(0, END)
        pass_box.delete(0, END)
    #removes all data entries
    def clear_records():
        for record in info_tree.get_children():
            info_tree.delete(record)
    #removes highlighted data entry
    def remove_selected():
        for record in info_tree.selection():
            info_tree.delete(record)

        
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