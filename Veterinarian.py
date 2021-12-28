import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from window import *
from dbcontrol import *


class AnimalInfo(ttk.Frame):  # to be used tab
    def __init__(self, container):
        super().__init__(container)

        def check_to_fill():
            def no_custo():
                search_answer.set("No customer found")
                firstname_info["state"] = "normal"
                firstname_info.delete("1.0", "end-1c")
                firstname_info["state"] = "disable"

                lastname_info["state"] = "normal"
                lastname_info.delete("1.0", "end-1c")
                lastname_info["state"] = "disable"

                phone_info["state"] = "normal"
                phone_info.delete("1.0", "end-1c")
                phone_info["state"] = "disable"

                animal_name_info["state"] = "normal"
                animal_name_info.delete("1.0", "end-1c")
                animal_name_info["state"] = "disable"

                animal_type_info["state"] = "normal"
                animal_type_info.delete("1.0", "end-1c")
                animal_type_info["state"] = "disable"

                animal_important_info["state"] = "normal"
                animal_important_info.delete("1.0", "end-1c")
                animal_important_info["state"] = "disable"
                list_select.delete(0, tk.END)

            found_username = Search(enter_username.get("1.0","end-1c"))
            if not found_username:
                no_custo()
            elif found_username[6] != "Customer":
                no_custo()

            else:
                search_answer.set("")

                firstname_info["state"] = "normal"
                firstname_info.delete("1.0", "end-1c")
                firstname_info.insert(tk.END, found_username[1])
                firstname_info["state"] = "disable"

                lastname_info["state"] = "normal"
                lastname_info.delete("1.0", "end-1c")
                lastname_info.insert(tk.END, found_username[2])
                lastname_info["state"] = "disable"

                phone_info["state"] = "normal"
                phone_info.delete("1.0", "end-1c")
                phone_info.insert(tk.END, '0'+found_username[4])
                phone_info["state"] = "disable"

                animal_name_info["state"] = "normal"
                animal_name_info.delete("1.0", "end-1c")
                animal_name_info["state"] = "disable"

                animal_type_info["state"] = "normal"
                animal_type_info.delete("1.0", "end-1c")
                animal_type_info["state"] = "disable"

                animal_important_info["state"] = "normal"
                animal_important_info.delete("1.0", "end-1c")
                animal_important_info["state"] = "disable"

                nonlocal animal_list
                animal_list = AnimalName(found_username[0])
                list_select.delete(0, tk.END)
                for item in animal_list:
                    list_select.insert(tk.END, item)


        def animal_select(x=None):
            found_username = Search(enter_username.get("1.0", "end-1c"))
            index = list_select.curselection()
            found_animal_info = animal_details(found_username[0], list_select.get(index))
            animal_name_info["state"] = "normal"
            animal_name_info.delete("1.0", "end-1c")
            animal_name_info.insert(tk.END, found_animal_info[1])
            animal_name_info["state"] = "disable"

            animal_type_info["state"] = "normal"
            animal_type_info.delete("1.0", "end-1c")
            animal_type_info.insert(tk.END, found_animal_info[0])
            animal_type_info["state"] = "disable"

            animal_important_info["state"] = "normal"
            animal_important_info.delete("1.0", "end-1c")
            animal_important_info.insert(tk.END, found_animal_info[2])
            animal_important_info["state"] = "disable"

        user_select_frame = ttk.Frame(self)
        user_select_frame.grid(pady=20)
        search_answer = tk.StringVar()
        enter_username = tk.Text(user_select_frame, height=1, width=20)
        enter_username.grid(row=0, column=0, padx=30)
        enter_username.insert("1.0", "Enter username here")
        username_choose = ttk.Button(user_select_frame, text="Search", command=check_to_fill).grid(row=0, column=1)
        ttk.Label(user_select_frame, textvariable=search_answer, foreground="red").grid(row=1, column=0, padx=10,
                                                                                        sticky="E")
        separator = ttk.Separator(self, orient='horizontal').grid(rowspan=2, sticky="EW")

        user_output_frame = ttk.Frame(self)
        user_output_frame.grid(pady=20)
        ttk.Label(user_output_frame, text="First Name: ").grid(row=0, column=0, padx=20)
        firstname_info = tk.Text(user_output_frame, state='disabled', height=1, width=20)
        firstname_info.grid(row=0, column=1, padx=30)

        ttk.Label(user_output_frame, text="Last Name: ").grid(row=1, column=0, padx=20, pady=20)
        lastname_info = tk.Text(user_output_frame, state='disabled', height=1, width=20)
        lastname_info.grid(row=1, column=1, padx=30)

        ttk.Label(user_output_frame, text="Phone No.: ").grid(row=2, column=0, padx=20)
        phone_info = tk.Text(user_output_frame, state='disabled', height=1, width=20)
        phone_info.grid(row=2, column=1, padx=30)


        ttk.Label(user_output_frame, text="Animals: ").grid(row=3, column=0, padx=20, pady=20)
        animal_list = ()
        list_var = tk.StringVar(value=animal_list)
        list_select = tk.Listbox(user_output_frame, listvariable=list_var, height=len(animal_list))
        list_select.grid(row=3, column=1, padx=20, pady=20)
        list_select.bind('<<ListboxSelect>>', animal_select)

        animal_output_frame = ttk.Frame(self)
        animal_output_frame.grid(pady=20)
        ttk.Label(animal_output_frame, text="Animal Name: ").grid(row=0, column=0, padx=20, pady=20)
        animal_name_info = tk.Text(animal_output_frame, state='disabled', height=1, width=20)
        animal_name_info.grid(row=0, column=1, padx=30)

        ttk.Label(animal_output_frame, text="Animal Type: ").grid(row=1, column=0, padx=20)
        animal_type_info = tk.Text(animal_output_frame, state='disabled', height=1, width=20)
        animal_type_info.grid(row=1, column=1, padx=30)

        ttk.Label(self, text="Important Info: ").grid(padx=20, pady=10)
        animal_important_info = tk.Text(self, state='disabled', height=1, width=40)
        animal_important_info.grid(padx=30, pady=10)

        ttk.Label(self, text="").grid(padx=20, pady=10)



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
        if_logout_v_window.protocol("WM_DELETE_WINDOW", cancel_to_logout)

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
    info_of_animal_tab = AnimalInfo(tabs)
    tabs.add(info_of_animal_tab, text=" Animal Info ")

    vet_window.mainloop()