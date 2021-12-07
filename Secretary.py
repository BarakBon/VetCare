import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from window import *
from dbcontrol import *


class SignupTab(ttk.Frame):  # first tab - signup
    def __init__(self, container):
        super().__init__(container)

        def get_register_data():  # gets from the entries the data the user inserted
            def user_created_window():  # the window that says the user signed up
                created_alert = tk.Tk()
                created_alert.title("Success")
                created_alert.resizable(False, False)
                set_window(created_alert)
                ttk.Label(created_alert, text="User created successfully. ", foreground="green").grid(row=0,column=0,padx=30,pady=20)

                ttk.Button(created_alert, text="OK", command=created_alert.destroy).grid(ipadx=10, ipady=5, pady=10)
                created_alert.protocol("WM_DELETE_WINDOW", created_alert.destroy)


            if username_inserted.get() is "" or password_inserted.get() is "" or firstname_inserted.get() is "" or lastname_inserted.get() is ""\
                    or city_inserted.get() is "" or phone_inserted.get() is "" or email_inserted.get() is "" or type_selected.get() is "":  # check if one of the entries is empty
                register_mistake.set("Fill all slots please")
            else:  # sends the data to the database
                flag = newcustomer(username_inserted.get(),password_inserted.get(),firstname_inserted.get(),lastname_inserted.get(),
                            city_inserted.get(),phone_inserted.get(),email_inserted.get(),type_selected.get())
                if flag is -1:
                    register_mistake.set("Username already exist")
                else:
                    register_mistake.set("")
                    user_created_window()


        # enteries and vars for the registerations process
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

        # the label that says if there is a mistake at the user input
        ttk.Label(self, textvariable=register_mistake, foreground="red").grid(row=8, column=1, padx=10, sticky="W")

        register_button = ttk.Button(self, text="Register", command=get_register_data)
        register_button.grid(row=9, column=1, ipady=3, ipadx=10, pady=20, sticky="W")


class UserInfo(ttk.Frame):  # second tab - user info
    def __init__(self, container):
        super().__init__(container)

        def check_to_fill():
            
            search_answer.set("No username found")

        user_select_frame = ttk.Frame(self)
        user_select_frame.grid(pady=20)
        search_answer = tk.StringVar()
        enter_username = tk.Text(user_select_frame, height=1, width=20)
        enter_username.grid(row=0, column=0, padx=30)
        enter_username.insert("1.0", "Enter username here")
        username_choose = ttk.Button(user_select_frame, text="Search", command=check_to_fill).grid(row=0, column=1)
        ttk.Label(user_select_frame, textvariable=search_answer, foreground="red").grid(row=1, column=0, padx=10, sticky="E")

        separator = ttk.Separator(self, orient='horizontal').grid(columnspan=2, sticky="EW")




def secretary_main(id):  # main secretary window setup
    # window setup
    secretary_window = tk.Tk()
    secretary_window.title("VetCare  -  Secretary")
    secretary_window.resizable(False, False)
    set_window(secretary_window)
    secretary_window.columnconfigure(0, weight=1)
    # secretary_window.rowconfigure(1, weight=1)

    def s_logout():  # take care on the logout process
        if_logout_s_window = tk.Tk()
        if_logout_s_window.title("Success")
        if_logout_s_window.resizable(False, False)
        set_window(if_logout_s_window)
        ttk.Label(if_logout_s_window, text="Are you sure you want to logout? ").grid(row=0, column=0, padx=30,pady=10)
        ttk.Label(if_logout_s_window, text="All unsaved actions will be deleted. ", foreground="red").grid(row=1, column=0, padx=30, pady=5)
        logout_approve_frame = ttk.Frame(if_logout_s_window)
        logout_approve_frame.grid(row=2, column=0, pady=10)

        def yes_to_logout():  # if the user agreed to logout
            if_logout_s_window.destroy()
            secretary_window.destroy()

        #  the buttons to agree or not to logout
        ttk.Button(logout_approve_frame, text="Yes", command=yes_to_logout).grid(row=0, column=0, ipadx=5, ipady=2, padx=5)
        ttk.Button(logout_approve_frame, text="Cancel", command=if_logout_s_window.destroy).grid(row=0, column=1, ipadx=5,ipady=2, padx=5)



    # custom style for the logout button
    style = ttk.Style(secretary_window)
    style.map("CustomButton.TButton", foreground=[("!pressed", "red")], backround=[("!pressed", "red")])

    # logged in top bar title and logout button in frame
    logged_bar_frame = ttk.Frame(secretary_window).grid(sticky="EW")
    ttk.Label(logged_bar_frame, text=("Hello,   "+ UserID_to_First_Name(id))).grid(row=0, column=0, padx=20, pady=10, sticky="W")
    logout_button = ttk.Button(logged_bar_frame, text="Log Out", style="CustomButton.TButton",command=s_logout)
    logout_button.grid(row=0, column=0, padx=10, pady=10, sticky="E")
    secretary_window.protocol("WM_DELETE_WINDOW", s_logout)

    # tabs creations
    tabs = ttk.Notebook(secretary_window)
    # tabs.columnconfigure(0, weight=1)
    tabs.grid(sticky="EW")
    register_new_user_tab = SignupTab(tabs)
    tabs.add(register_new_user_tab, text="Signup")
    info_of_user = UserInfo(tabs)
    tabs.add(info_of_user, text="Info")

    secretary_window.mainloop()



