import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from window import *
from dbcontrol import *


class SignupTab(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        def get_register_data():  # gets from the function that its
            def user_created_window():
                created_alert = tk.Tk()
                created_alert.title("Success")
                created_alert.resizable(False, False)
                set_window(created_alert)
                ttk.Label(created_alert, text="User created successfully. ", foreground="green").grid(row=0,column=0,padx=30,pady=20)

                ttk.Button(created_alert, text="OK", command=created_alert.destroy).grid(ipadx=10, ipady=5, pady=10)
                created_alert.protocol("WM_DELETE_WINDOW", created_alert.destroy)


            if username_inserted.get() is "" or password_inserted.get() is "" or firstname_inserted.get() is "" or lastname_inserted.get() is ""\
                    or city_inserted.get() is "" or phone_inserted.get() is "" or email_inserted.get() is "" or type_selected.get() is "":
                register_mistake.set("Fill all slots please")
            else:
                flag = newcustomer(username_inserted.get(),password_inserted.get(),firstname_inserted.get(),lastname_inserted.get(),
                            city_inserted.get(),phone_inserted.get(),email_inserted.get(),type_selected.get())
                if flag is -1:
                    register_mistake.set("Username already exist")
                else:
                    register_mistake.set("")
                    user_created_window()



        firstname_inserted = tk.StringVar()
        lastname_inserted = tk.StringVar()
        email_inserted = tk.StringVar()
        city_inserted = tk.StringVar()
        phone_inserted = tk.StringVar()
        username_inserted = tk.StringVar()
        password_inserted = tk.StringVar()
        type_selected = tk.StringVar()
        register_mistake = tk.StringVar()

        ttk.Label(self, text="First name: ").grid(row=0, column=0, padx=10, pady=20)
        firstname_entry = ttk.Entry(self, width=20, textvariable=firstname_inserted)
        firstname_entry.grid(row=0, column=1, pady=10, padx=20)

        ttk.Label(self, text="Last name: ").grid(row=1, column=0, padx=10)
        lastname_entry = ttk.Entry(self, width=20, textvariable=lastname_inserted)
        lastname_entry.grid(row=1, column=1, pady=10)

        ttk.Label(self, text="Email: ").grid(row=2, column=0, padx=10, pady=20)
        email_entry = ttk.Entry(self, width=20, textvariable=email_inserted)
        email_entry.grid(row=2, column=1, pady=10)

        ttk.Label(self, text="City: ").grid(row=3, column=0, padx=10, pady=15)
        city_entry = ttk.Entry(self, width=20, textvariable=city_inserted)
        city_entry.grid(row=3, column=1, pady=10)

        ttk.Label(self, text="Phone number: ").grid(row=4, column=0, padx=10, pady=20)
        phone_entry = ttk.Entry(self, width=20, textvariable=phone_inserted)
        phone_entry.grid(row=4, column=1, pady=10)

        ttk.Label(self, text="Username: ").grid(row=5, column=0, padx=10, pady=20)
        username_entry = ttk.Entry(self, width=20, textvariable=username_inserted)
        username_entry.grid(row=5, column=1, pady=10)

        ttk.Label(self, text="Password: ").grid(row=6, column=0, padx=10, pady=20)
        password_entry = ttk.Entry(self, width=20, textvariable=password_inserted)
        password_entry.grid(row=6, column=1, pady=10)

        ttk.Label(self, text="Type: ").grid(row=7, column=0, padx=10, pady=20)
        type_list = ttk.Combobox(self, textvariable=type_selected)
        type_list["values"] = ("Veterinarian", "Secretary", "Customer")
        type_list["state"] = "readonly"
        type_list.grid(row=7, column=1, padx=10, pady=20)
        # to get the combo select: type_selected.get()

        ttk.Label(self, textvariable=register_mistake, foreground="red").grid(row=8, column=1, padx=10, sticky="W")

        register_button = ttk.Button(self, text="Register", command=get_register_data)
        register_button.grid(row=9, column=1, ipady=3, ipadx=10, pady=20, sticky="W")



def secretary_main(id):
    # window setup
    secretary_window = tk.Tk()
    secretary_window.title("VetCare  -  Secretary")
    secretary_window.resizable(True, True)
    set_window(secretary_window)
    secretary_window.columnconfigure(0, weight=1)
    # secretary_window.rowconfigure(1, weight=1)


    # custom style for the logout button
    style = ttk.Style(secretary_window)
    style.map("CustomButton.TButton", foreground=[("!pressed", "red")], backround=[("!pressed", "red")])

    # logged in top bar title and logout button in frame
    logged_bar_frame = ttk.Frame(secretary_window).grid(sticky="EW")
    ttk.Label(logged_bar_frame, text=("Hello,   "+ UserID_to_First_Name(id))).grid(row=0, column=0, padx=20, pady=10, sticky="W")
    logout_button = ttk.Button(logged_bar_frame, text="Log Out", style="CustomButton.TButton",
                               command=secretary_window.destroy)
    logout_button.grid(row=0, column=0, padx=10, pady=10, sticky="E")

    # tabs creations
    tabs = ttk.Notebook(secretary_window)
    # tabs.columnconfigure(0, weight=1)
    tabs.grid(sticky="EW")
    register_new_user_tab = SignupTab(tabs)
    tabs.add(register_new_user_tab, text="Signup")

    secretary_window.mainloop()



