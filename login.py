import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from window import *

class LoginScreenData(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # window settings
        self.title("Login")
        self.resizable(False, False)
        set_window(self)
        self.columnconfigure(0, weight=1)

        # the logo creation and label
        logo = Image.open("logo1.png").resize((340, 115))
        logo_picture = ImageTk.PhotoImage(logo)
        logo_label = ttk.Label(self, image=logo_picture)
        logo_label.image = logo_picture
        logo_label.grid(row=0, column=0)

        # username and password frame creation
        login_info = ttk.Frame(self)
        login_info.grid(pady=40)
        login_info.columnconfigure(0, weight=1)

        # the login insertion guides and insert boxes
        username_inserted = tk.StringVar()
        password_inserted = tk.StringVar()
        ttk.Label(login_info, text="Username: ").grid(row=0, column=0, padx=10)
        username_entry = ttk.Entry(login_info, width=20, textvariable=username_inserted)
        username_entry.grid(row=0, column=1, pady=10, padx=20)
        ttk.Label(login_info, text="Password: ").grid(row=1, column=0, padx=10)
        password_entry = ttk.Entry(login_info,  width=20, textvariable=password_inserted)
        password_entry.grid(row=1, column=1, pady=10)


        def check_login():  # checks if the user exist (in the future)
            print(username_inserted.get())
            print(password_inserted.get())
            login_button["state"] = "disabled"
            error_warning()



        def error_warning():  # display error massage for incorect user and disable the login unless the butten pressed
            def try_again():  # return the login to function and removes the error window
                error.destroy()
                login_button["state"] = "normal"

            # creates the error window
            error = tk.Tk()
            error.title("Error")
            error.resizable(False, False)
            set_window(error)
            ttk.Label(error, text="Wrong password / username, please try again. ").grid(row=0, column=0, padx=30, pady=20)
            ttk.Button(error, text="Try again", command=try_again).grid(ipadx=10, ipady=5, pady=10)


        # login button to get the login details and check them
        login_button = ttk.Button(self, text="Login", command=check_login)
        login_button.grid(ipadx=10, ipady=5, pady=20)




login = LoginScreenData()
login.mainloop()