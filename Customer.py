import time
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from window import *
from dbcontrol import *
from tkcalendar import Calendar
import datetime

class MakeAppointment(ttk.Frame):  # to be used tab
    def __init__(self, container):
        super().__init__(container)

        def day_chose(x=None):
            print("day selected")

        ttk.Label(self, text="Select Date: ").grid(row=0, column=0, padx=10, pady=20)

        cal = Calendar(self, selectmode="day", firstweekday="sunday", mindate=datetime.date.today(), weekendbackground="white")
        cal.grid(ipadx=80, ipady=30, padx=20, sticky="EW")
        cal.bind('<<CalendarSelected>>', day_chose)



def customer_main(id):  # main customer window setup
    # window setup
    customer_window = tk.Tk()
    customer_window.title("VetCare  -  Customer")
    customer_window.resizable(True, True)
    set_window(customer_window)
    customer_window.columnconfigure(0, weight=1)


    # custom style for the logout button
    style = ttk.Style(customer_window)
    style.map("CustomButton.TButton", foreground=[("!pressed", "red")], backround=[("!pressed", "red")])

    def c_logout():  # take care on the logout process
        if_logout_c_window = tk.Tk()
        if_logout_c_window.title("Warning")
        if_logout_c_window.resizable(False, False)
        set_window(if_logout_c_window)
        logout_button["state"] = "disable"
        ttk.Label(if_logout_c_window, text="Are you sure you want to logout? ").grid(row=0, column=0, padx=30,pady=10)
        ttk.Label(if_logout_c_window, text="All unsaved actions will be deleted. ", foreground="red").grid(row=1, column=0, padx=30, pady=5)
        logout_approve_frame = ttk.Frame(if_logout_c_window)
        logout_approve_frame.grid(row=2, column=0, pady=10)

        def yes_to_logout():  # if the user agreed to logout
            if_logout_c_window.destroy()
            customer_window.destroy()

        def cancel_to_logout():  # if the user cancel the logout
            if_logout_c_window.destroy()
            logout_button["state"] = "normal"

        # logged in top bar title and logout button in frame
        ttk.Button(logout_approve_frame, text="Yes", command=yes_to_logout).grid(row=0, column=0, ipadx=5, ipady=2, padx=5)
        ttk.Button(logout_approve_frame, text="Cancel", command=cancel_to_logout).grid(row=0, column=1, ipadx=5,ipady=2, padx=5)

    def c_no_exit():
        pass

    # logged in top bar title and logout button in frame
    logged_bar_frame = ttk.Frame(customer_window).grid(sticky="EW")
    ttk.Label(logged_bar_frame, text=("Hello,   "+ UserID_to_First_Name(id))).grid(row=0, column=0, padx=20, pady=10, sticky="W")
    logout_button = ttk.Button(logged_bar_frame, text="Log Out", style="CustomButton.TButton",command=c_logout)
    logout_button.grid(row=0, column=0, padx=10, pady=10, sticky="E")
    customer_window.protocol("WM_DELETE_WINDOW", c_no_exit)

    # tabs creations
    tabs = ttk.Notebook(customer_window)
    # tabs.columnconfigure(0, weight=1)
    tabs.grid(sticky="EW")
    register_new_user_tab = MakeAppointment(tabs)
    tabs.add(register_new_user_tab, text="Make Appointment")

    customer_window.mainloop()