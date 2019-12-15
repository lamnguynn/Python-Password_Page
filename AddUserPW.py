import tkinter as tk
import pickle

r = tk.Tk()
r.title('New Account')

def add_to_user_database():
    import PasswordPage as pwpage                                #Import the PasswordPage file in order to get access to the dictionary holding the logins
    pwpage.user_data[E1.get()] = E2.get()                        #Adding a new entry into the dictionary
    pickle.dump(pwpage.user_data, open('login_info.dat', 'wb'))  #Save to the computer by creating a file in binary
    r.withdraw()

#Creating the widgets
L1 = tk.Label(r,text='Enter New Username:').grid(row=0)
L2 = tk.Label(r,text = 'Enter New Password:').grid(row=1)
E1 = tk.Entry(r)
E2 = tk.Entry(r)
B1 = tk.Button(r, text = 'Submit',width=12,command = add_to_user_database).grid(row=2, column=1)
B2 = tk.Button(r, text = 'Cancel',width=12,command = r.withdraw).grid(row=3, column=1)

#Placing the entry widgets
E1.grid(row = 0, column = 1)
E2.grid(row = 1, column = 1)

tk.mainloop()
