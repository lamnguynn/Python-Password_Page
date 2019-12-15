import tkinter as tk
import pickle
r = tk.Tk()
r.title('Forgot Password')


def new_password():
    import PasswordPage as pwdpge
    for i in pickle.load(open('login_info.dat','rb')).keys():
        if i == E1.get():
            pwdpge.user_data[i] = E2.get()
            pickle.dump(pwdpge.user_data,open('login_info.dat', 'wb'))  # Save to the computer by creating a file in binary
            r.withdraw()
            break
        else:
            unsuccessful_change_label = tk.Label(r, text="Try Again!").grid(row=2, column=0)

#Creating the widgets
L1 = tk.Label(r,text='Enter Username:').grid(row=0)
L2 = tk.Label(r,text = 'Enter New Password:').grid(row=1)
E1 = tk.Entry(r)
E2 = tk.Entry(r)
B1 = tk.Button(r, text = 'Submit',width=12,command = new_password).grid(row=2, column=1)
B2 = tk.Button(r, text = 'Cancel',width=12,command = r.withdraw).grid(row=3, column=1)

#Placing the entry widgets
E1.grid(row = 0, column = 1)
E2.grid(row = 1, column = 1)

tk.mainloop()
