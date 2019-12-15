import tkinter as tk
import pickle

'''
Author: Lam Nguyen
Date: 12/15/2019
Contact: lam65nguyen@tamu.edu
Notes: Any questions or confusion please let me know! 

The purpose of this program is to create a window from tkinter GUI to prompt the user to enter their username and create a new password. 
It will prompt the user that their inputted username is wrong if it is not found in the file holding the logins.
Key Ideas: Access a file in order to get and verify login information.
           Work with pulling data from other files. 
           Work with tkinter GUI.
'''
r = tk.Tk()
r.title('Forgot Password')


def new_password():
    '''Purpose of this function is to check the file holding the login information to see if the user can create a new password. If so, create it.'''
    import LoginPage as login                                               #Importing code from LoginPage.py in order to have access to the dictionary holding the login information
    for i in pickle.load(open('login_info.dat','rb')).keys():               #Traverse the keys of the dictionary inside the file.
        if i == E1.get():                                                   #If one of the keys in the file matches the user's inputted username, create a new password.
            login.user_data[i] = E2.get()
            pickle.dump(login.user_data,open('login_info.dat', 'wb'))
            r.withdraw()                                                    #Hide the GUI after all the code above is done.
            break
        else:                                                               #If the user inputted username is not found, print a label on the GUI
            unsuccessful_change_label = tk.Label(r, text="Incorrect Username!").grid(row=2, column=0)

#Creating the widgets
L1 = tk.Label(r,text='Enter Username:').grid(row=0)             #Label for username
L2 = tk.Label(r,text = 'Enter New Password:').grid(row=1)       #Label for password
E1 = tk.Entry(r)                                                #Entry for user to type in their username. Placed right beside L1 on the grid.
E2 = tk.Entry(r)                                                #Entry for user to type in their new password. Placed right beside L2 on the grid.
B1 = tk.Button(r, text = 'Submit',width=12,command = new_password).grid(row=2, column=1)            #Button for user to submit the username and password
B2 = tk.Button(r, text = 'Cancel',width=12,command = r.withdraw).grid(row=3, column=1)              #Button for user to cancel

#Placing the entry widgets
E1.grid(row = 0, column = 1)
E2.grid(row = 1, column = 1)

tk.mainloop()
