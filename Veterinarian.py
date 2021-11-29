import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from window import *
from dbcontrol import *


class FutureTab(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        ttk.Label(self, text="this is the main screen of the veterinarian. ").grid(row=0, column=0, padx=10, pady=20)






def veterinarian_main(id):
    # window setup
    vet_window = tk.Tk()
    vet_window.title("VetCare  -  Veterinarian")
    vet_window.resizable(True, True)
    set_window(vet_window)
    vet_window.columnconfigure(0, weight=1)
    # secretary_window.rowconfigure(1, weight=1)


    # custom style for the logout button
    style = ttk.Style(vet_window)
    style.map("CustomButton.TButton", foreground=[("!pressed", "red")], backround=[("!pressed", "red")])

    # logged in top bar title and logout button in frame
    logged_bar_frame = ttk.Frame(vet_window).grid(sticky="EW")
    ttk.Label(logged_bar_frame, text=("Hello,   "+ UserID_to_First_Name(id))).grid(row=0, column=0, padx=20, pady=10, sticky="W")
    logout_button = ttk.Button(logged_bar_frame, text="Log Out", style="CustomButton.TButton",command=vet_window.destroy)
    logout_button.grid(row=0, column=0, padx=10, pady=10, sticky="E")

    # tabs creations
    tabs = ttk.Notebook(vet_window)
    # tabs.columnconfigure(0, weight=1)
    tabs.grid(sticky="EW")
    register_new_user_tab = FutureTab(tabs)
    tabs.add(register_new_user_tab, text="To be created")

    vet_window.mainloop()