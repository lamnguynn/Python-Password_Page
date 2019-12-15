import tkinter as tk
import pickle                       #Used to save data onto the computer
import os

os.system('cls')
print('\b\b')                       #Get rid of question symbol that appears

#Setting up the GUI
r = tk.Tk()
r.title("Login")

user_data = {"xyz": 'pwd123'}       #Dictionary to store username as the key and password as the value.

def check_login():
    '''This function checks to see if the username and password inputted from user is correct.'''
    for i in pickle.load(
            open('login_info.dat', 'rb')).keys():                                                           # Traverses the user_data keys to find the username first
        if i == gui_login[2].get() and pickle.load(open('login_info.dat', 'rb'))[i] == gui_login[3].get():  # Then if the username is found, then check to see if the password matches.
            successful_login_label = tk.Label(r, text="Loading...").grid(row=3)                             # If found, then print a message to the screen and destory the GUI
            print("Welcome!")
            r.destroy()
            return                                                                                          # Return is added because it should leave the function if the if statement is true.
        unsuccessful_login_label = tk.Label(r, text="Try Again!").grid(row=4,column=1)                      # If there is no such username found, then a label will appear to say error.

def new_user():
    '''This function will display a GUI to create a new account'''
    import AddUserPW as addNew
    addNew.r.deiconify() #show the widget

def forgot_password():
    '''This function will display a GUI to create a new password'''
    import ForgotPW as forPW
    forPW.r.deiconify() #show the widget

#Creating the widgets
gui_login = [tk.Label(r, text = "Username:").grid(row=0, column = 0),                   #Storing the buttons, text, and entries into a list for better data management.
             tk.Label(r, text = "Password:").grid(row=1, column = 0),
             tk.Entry(r),
             tk.Entry(r),
             tk.Button(r, text = "Enter", width = 16,command = check_login).grid(row = 2, column  = 1),
             tk.Button(r, text = "Press to quit", command = quit).grid(row = 2, column  = 0),
             tk.Button(r, text = "Sign up",width = 9,command = new_user).grid(row=3,column=0),
             tk.Button(r, text = "Forgot Password?",width = 16, command = forgot_password).grid(row=3,column=1)]

gui_login[2].grid(row = 0, column = 1)
gui_login[3].grid(row = 1, column = 1)

r.mainloop()
done = True                                                                             #Since there is a loop that will break when the GUI is destroyed (right password and username), there should be a new variable that can be accessed by other files to see.
