import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
# from windows import

class LoginScreenData(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # window settings
        self.title("Login")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        style = ttk.Style(self)
        style.theme_use("clam")

        #  position the screen at the middle of the screen
        windowWidth = self.winfo_reqwidth()
        windowHeight = self.winfo_reqheight()

        # Gets both half the screen width/height and window width/height
        positionRight = int(self.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(self.winfo_screenheight() / 2.5 - windowHeight / 2)

        # Positions the window in the center of the page.
        self.geometry("+{}+{}".format(positionRight, positionDown))

        # the logo creation and label
        logo = Image.open("logo1.png").resize((340, 115))
        logo_picture = ImageTk.PhotoImage(logo)
        logo_label = ttk.Label(self, image=logo_picture)
        logo_label.image = logo_picture
        logo_label.grid(row=0, column=0)
        # greeting_text = ttk.Label(self, text="Welcome to VetCare")
        # greeting_text.config(font=('', 20))
        # greeting_text.grid(row=0, column=0, pady=20, padx=20)

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

        # login button to get the login details and check them
        login_button = ttk.Button(self, text="Login", command=check_login)
        login_button.grid(ipadx=10, ipady=5, pady=20)





class LoginButtons(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



login = LoginScreenData()
login.mainloop()