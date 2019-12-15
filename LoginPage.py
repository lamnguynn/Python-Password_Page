import tkinter as tk
import pickle
import os

'''
Author: Lam Nguyen
Date: 12/15/2019
Contact: lam65nguyen@tamu.edu
Notes: Any questions or confusion please let me know! 

The purpose of this program is to create a login page with tkinter GUI.
Key Ideas: Import other python files to use with combination with code from current file.
           Work with tkinter GUI.
           Saving data into a file and accessing it. 
           
Possible Improvements:
           Using CSS to create a more appealing GUI
           Add an encryption to the login information for security
'''
os.system('cls')
r = tk.Tk()
r.title("Login")

#pickle.dump({"xyz":'pwd123'},open('login_info.dat','wb'))                                                  #Uncomment if you are first using this program. Run the program, exit, and then comment it. 

user_data = pickle.load(open('login_info.dat','rb'))                                                        # Dictionary to store username as the key and password as the value.

def check_login():
    '''This function checks to see if the username and password inputted from user is correct.'''
    for i in pickle.load(open('login_info.dat', 'rb')).keys():                                              # Traverses the user_data keys to find the username first
        if i == gui_login[2].get() and pickle.load(open('login_info.dat', 'rb'))[i] == gui_login[3].get():  # Then if the username is found, then check to see if the password matches.
            successful_login_label = tk.Label(r, text="Loading...").grid(row=3)                             # If found, then print a message to the screen and destory the GUI
            print("Welcome!")
            r.destroy()
            return                                                                                          # Return is added because it should leave the function if the if statement is true.
        unsuccessful_login_label = tk.Label(r, text="Try Again!").grid(row=4,column=1)                      # If there is no such username found, then a label will appear to say error.

def new_user():
    '''This function will display a GUI to create a new account when called.'''
    import AddUserPW as addNew  #Importing the python file AddUserPW to prompt user to create new username and password
    addNew.r.deiconify()        #show the widget

def forgot_password():
    '''This function will display a GUI to create a new password when called'''
    import ForgotPW as forPW    #Importing the python file ForgotPW to prompt user to create a new password
    forPW.r.deiconify()         #show the widget

'''Storing the widgets into a list. Really no reason to, but I wanted to play around with retrieving data.'''
gui_login = [tk.Label(r, text = "Username:").grid(row=0, column = 0),                                               # Label for username.
             tk.Label(r, text = "Password:").grid(row=1, column = 0),                                               # Label for password.
             tk.Entry(r),                                                                                           # Entry for user to type in their new username. Placed right beside the username label on the grid.
             tk.Entry(r),                                                                                           # Entry for user to type in their new password. Placed right beside the password label on the grid.
             tk.Button(r, text = "Enter", width = 16,command = check_login).grid(row = 2, column  = 1),             # Button for user to login.
             tk.Button(r, text = "Press to quit", command = quit).grid(row = 2, column  = 0),                       # Button for user to exit out the program.
             tk.Button(r, text = "Sign up",width = 9,command = new_user).grid(row=3,column=0),                      # Button for user to create a new account.
             tk.Button(r, text = "Forgot Password?",width = 16, command = forgot_password).grid(row=3,column=1)]    # Button for user to create a new password if they forgot.

gui_login[2].grid(row = 0, column = 1)
gui_login[3].grid(row = 1, column = 1)

r.mainloop()

'''Since when the user logins in the code is essentially done, there will be a new variable created below to sign completion.'''
done = True
