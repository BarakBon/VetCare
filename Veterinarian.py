import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from window import *
from dbcontrol import *


class FutureTab(ttk.Frame):  # to be used tab
    def __init__(self, container):
        super().__init__(container)

        ttk.Label(self, text="this is the main screen of the veterinarian. ").grid(row=0, column=0, padx=10, pady=20)






def veterinarian_main(id): # main veterinarian window setup
    # window setup
    vet_window = tk.Tk()
    vet_window.title("VetCare  -  Veterinarian")
    vet_window.resizable(True, True)
    set_window(vet_window)
    vet_window.columnconfigure(0, weight=1)


    # custom style for the logout button
    style = ttk.Style(vet_window)
    style.map("CustomButton.TButton", foreground=[("!pressed", "red")], backround=[("!pressed", "red")])

    def v_logout():  # take care on the logout process
        if_logout_v_window = tk.Tk()
        if_logout_v_window.title("Success")
        if_logout_v_window.resizable(False, False)
        set_window(if_logout_v_window)
        logout_button["state"] = "disable"
        ttk.Label(if_logout_v_window, text="Are you sure you want to logout? ").grid(row=0, column=0, padx=30,pady=10)
        ttk.Label(if_logout_v_window, text="All unsaved actions will be deleted. ", foreground="red").grid(row=1, column=0, padx=30, pady=5)
        logout_approve_frame = ttk.Frame(if_logout_v_window)
        logout_approve_frame.grid(row=2, column=0, pady=10)

        def yes_to_logout():  # if the user agreed to logout
            if_logout_v_window.destroy()
            vet_window.destroy()

        def cancel_to_logout():  # if the user cancel the logout
            if_logout_v_window.destroy()
            logout_button["state"] = "normal"

        #  the buttons to agree or not to logout
        ttk.Button(logout_approve_frame, text="Yes", command=yes_to_logout).grid(row=0, column=0, ipadx=5, ipady=2, padx=5)
        ttk.Button(logout_approve_frame, text="Cancel", command=cancel_to_logout).grid(row=0, column=1, ipadx=5,ipady=2, padx=5)

    def v_no_exit():
        pass

    # logged in top bar title and logout button in frame
    logged_bar_frame = ttk.Frame(vet_window).grid(sticky="EW")
    ttk.Label(logged_bar_frame, text=("Hello,   "+ UserID_to_First_Name(id))).grid(row=0, column=0, padx=20, pady=10, sticky="W")
    logout_button = ttk.Button(logged_bar_frame, text="Log Out", style="CustomButton.TButton",command=v_logout)
    logout_button.grid(row=0, column=0, padx=10, pady=10, sticky="E")
    vet_window.protocol("WM_DELETE_WINDOW", v_no_exit)

    # tabs creations
    tabs = ttk.Notebook(vet_window)
    # tabs.columnconfigure(0, weight=1)
    tabs.grid(sticky="EW")
    register_new_user_tab = FutureTab(tabs)
    tabs.add(register_new_user_tab, text="To be created")

    vet_window.mainloop()