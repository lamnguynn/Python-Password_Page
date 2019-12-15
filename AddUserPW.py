import tkinter as tk
import pickle

'''
Author: Lam Nguyen
Date: 12/15/2019
Contact: lam65nguyen@tamu.edu
Notes: Any questions or confusion please let me know!

The purpose of this program is to create a window from tkinter GUI to prompt the user to make a new account by inputting a username and password.
Key Ideas: Ultilize files in order to save user login information in. 
           Work with pulling data from other files. 
           Work with tkinter GUI.
'''

r = tk.Tk()
r.title('New Account')

def add_to_user_database():
    '''Purpose of this function is to add the inputted information from the user to the file holding login information'''
    import LoginPage as login                                   #Importing code from LoginPage.py in order to have access to the dictionary holding the login information
    for i in login.user_data.keys():                            #Travserses the keys of the dictionary inside the file to see if the username already exist.
        if i == E1.get():                                       #If so, then print a label and return nothing. That way the code below does not execute.
            already_exist_label = tk.Label(r, text = "Username already exist").grid(row = 3, column = 0)
            return
    login.user_data[E1.get()] = E2.get()                        #Add the user's username and password into the dictionary from LoginPage.py
    pickle.dump(login.user_data, open('login_info.dat', 'wb'))  #Save the dictionary from LoginPage.py to the file.
    r.withdraw()                                                #Hide the GUI after all the code above is done.

#Creating the widgets
L1 = tk.Label(r,text='Enter New Username:').grid(row=0)         #Label for username
L2 = tk.Label(r,text = 'Enter New Password:').grid(row=1)       #Label for password
E1 = tk.Entry(r)                                                #Entry for user to type in their new username. Placed right beside L1 on the grid.
E2 = tk.Entry(r)                                                #Entry for user to type in their new password. Placed right beside L2 on the grid.
B1 = tk.Button(r, text = 'Submit',width=12,command = add_to_user_database).grid(row=2, column=1)            #Button for user to submit the username and password
B2 = tk.Button(r, text = 'Cancel',width=12,command = r.withdraw).grid(row=3, column=1)                      #Button for user to cancel

#Placing the entry widgets
E1.grid(row = 0, column = 1)
E2.grid(row = 1, column = 1)

tk.mainloop()
