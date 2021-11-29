import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from window import *
from dbcontrol import *



class FutureTab(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        ttk.Label(self, text="this is the main screen of the customer. ").grid(row=0, column=0, padx=10, pady=20)






def customer_main(id):
    # window setup
    customer_window = tk.Tk()
    customer_window.title("VetCare  -  Customer")
    customer_window.resizable(True, True)
    set_window(customer_window)
    customer_window.columnconfigure(0, weight=1)
    # secretary_window.rowconfigure(1, weight=1)


    # custom style for the logout button
    style = ttk.Style(customer_window)
    style.map("CustomButton.TButton", foreground=[("!pressed", "red")], backround=[("!pressed", "red")])

    # logged in top bar title and logout button in frame
    logged_bar_frame = ttk.Frame(customer_window).grid(sticky="EW")
    ttk.Label(logged_bar_frame, text=("Hello,   "+ UserID_to_First_Name(id))).grid(row=0, column=0, padx=20, pady=10, sticky="W")
    logout_button = ttk.Button(logged_bar_frame, text="Log Out", style="CustomButton.TButton",command=customer_window.destroy)
    logout_button.grid(row=0, column=0, padx=10, pady=10, sticky="E")

    # tabs creations
    tabs = ttk.Notebook(customer_window)
    # tabs.columnconfigure(0, weight=1)
    tabs.grid(sticky="EW")
    register_new_user_tab = FutureTab(tabs)
    tabs.add(register_new_user_tab, text="To be created")

    customer_window.mainloop()