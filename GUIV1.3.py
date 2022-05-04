#Version 1.3 LMFAO
from tkinter import *
from tkinter import messagebox

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

    #username_entry.delete(0, END) #supposed to clear fields once successfully registered
    #password_entry.delete(0, END) #giving error at the moment

    #Label(registration_screen, text = "Registration Successful!", fg="green").pack()
    registration_screen.destroy()
    messagebox.showinfo(title="Success!", message="Account successfully created!")

def register():
    global registration_screen
    registration_screen = Toplevel(screen)
    registration_screen.title("CreateAccount")
    registration_screen.geometry("400x350")

    global username, username_entry, password, password_entry, color, color_entry, restaurant, restaurant_entry
    username = StringVar()
    password = StringVar()
    color = StringVar()
    restaurant = StringVar()

    Label(registration_screen, text= "Please enter your details below.").pack()
    Label(registration_screen, text= "").pack()
    Label(registration_screen, text= "Username *").pack()
    username_entry = Entry(registration_screen, textvariable= username).pack()
    Label(registration_screen, text= "Password *").pack()
    password_entry = Entry(registration_screen, textvariable= password).pack()
    Label(registration_screen, text= "").pack()
    Label(registration_screen, text= "Security Questions").pack()
    Label(registration_screen, text= "What is your favorite color?").pack()
    color_entry = Entry(registration_screen, textvariable= color).pack()
    Label(registration_screen, text= "What is your favorite restaurant?").pack()
    restaurant_entry = Entry(registration_screen, textvariable= restaurant).pack()
    Label(registration_screen, text= "").pack()
    Button(registration_screen, text = "Register", width= 10, height=1, command=register_user).pack()

def login():
    print("Login session started")
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