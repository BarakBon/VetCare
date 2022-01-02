import tkinter as tk
from tkinter import ttk
from window import *
from dbcontrol import *
import datetime

class AnimalInfo(ttk.Frame):  # first tab - see animal info
    def __init__(self, container):
        super().__init__(container)

        def check_to_fill():
            # checks if the user is found and fills or cleans the user and animal info in text boxes
            def no_custo():
                # cleans the spots because no customer has been found
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
                change_info_button["state"] = "disabled"

            found_username = Search(enter_username.get("1.0","end-1c"))
            if not found_username:
                no_custo()
            elif found_username[6] != "Customer":
                no_custo()

            else:
                # fills the slots only if customer user entered
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
                change_info_button["state"] = "disabled"

                nonlocal animal_list
                # fills the animal list of the user
                animal_list = AnimalName(found_username[0])
                list_select.delete(0, tk.END)
                for item in animal_list:
                    list_select.insert(tk.END, item)


        def animal_select(x=None):
            # when an animal is selected fills the info of him
            found_username = Search(enter_username.get("1.0", "end-1c"))
            index = list_select.curselection()
            nonlocal selected_animal
            if index:
                selected_animal = list_select.get(index)
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
                change_info_button["state"] = "normal"

        def change_important_info():
            # can change the important info of the animal
            found_username = Search(enter_username.get("1.0", "end-1c"))
            nonlocal selected_animal
            if selected_animal:
                found_animal_info = animal_details(found_username[0], selected_animal)
                set_important_note(found_username[0], found_animal_info[1], animal_important_info.get("1.0", "end-1c"))


        selected_animal = ""
        self.columnconfigure(0, weight=1)
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

        change_info_button = ttk.Button(self, text="Change Important Info", command=change_important_info)
        change_info_button.grid(ipadx=5,ipady=2, padx=5, pady=30)
        change_info_button["state"] = "disabled"


class NewTreatment(ttk.Frame):  # second tab - create new treatment
    def __init__(self, container):
        super().__init__(container)

        def check_to_fill():
            #  checks if the user is found and fills his animal list or cleans the text boxes if not
            def no_custo():
                search_answer.set("No customer found")
                treat_given.delete("1.0", "end")
                animal_list["values"] = None


            found_username = Search(enter_username.get("1.0", "end-1c"))
            if not found_username:
                no_custo()
            elif found_username[6] != "Customer":
                no_custo()

            else:
                #  only if the user is a customer fills the animal list
                search_answer.set("")
                animal_selected.set("")
                treat_given.delete("1.0", "end")
                animal_list["values"] = AnimalName(found_username[0])

        def create_treat():
            # creating a treatment after the user fills everything and clicks the button
            def treat_created_ok():
                # if the user clicked the ok button on the approve window
                create_treat_button["state"] = "normal"
                treat_created_alert.destroy()

            if animal_selected and treat_given.get("1.0", "end-1c"):
                # if all the slots are filled
                found_username = Search(enter_username.get("1.0", "end-1c"))
                set_treatments(found_username[0], animal_selected.get(), datetime.datetime.now().hour,
                                                        datetime.date.today(), treat_given.get("1.0", "end-1c"))
                create_treat_button["state"] = "disabled"
                # creates a popup window that says that the treatment has been created
                treat_created_alert = tk.Tk()
                treat_created_alert.title("Success")
                treat_created_alert.resizable(False, False)
                set_window(treat_created_alert)
                ttk.Label(treat_created_alert, text="Treatment saved successfully. ", foreground="green").grid(
                    row=0, column=0,
                    padx=30, pady=20)
                ttk.Button(treat_created_alert, text="OK", command=treat_created_ok).grid(ipadx=10, ipady=5,
                                                                                              pady=10)
                treat_created_alert.protocol("WM_DELETE_WINDOW", treat_created_ok)


        self.columnconfigure(0, weight=1)
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

        animal_selected = tk.StringVar()
        ttk.Label(self, text="Select Animal: ").grid(padx=10, pady=20)
        animal_list = ttk.Combobox(self, textvariable=animal_selected)
        animal_list["state"] = "readonly"
        animal_list.grid(padx=10)

        ttk.Label(self, text="Treatment Given: ").grid(padx=10, pady=30)
        treat_given = tk.Text(self, height=2, width=40)
        treat_given.grid()

        create_treat_button = ttk.Button(self, text="Save Treatment", command=create_treat)
        create_treat_button.grid(ipadx=5, ipady=2, pady=30)


class TreatmentRecord(ttk.Frame):  # third tab - see medical record of animal
    def __init__(self, container):
        super().__init__(container)

        def check_to_fill():
            #  fills the tree only if customer is entered and if not cleans everything
            def no_custo():
                #  no customer is found so cleans everything
                search_answer.set("No customer found")
                animal_list["values"] = None
                animal_selected.set("")
                treatments_tree.delete(*treatments_tree.get_children())


            found_username = Search(enter_username.get("1.0", "end-1c"))
            if not found_username:
                no_custo()
            elif found_username[6] != "Customer":
                no_custo()

            else:
                # only if a customer cleans the errors and fill animal list of the user
                search_answer.set("")
                animal_selected.set("")
                treatments_tree.delete(*treatments_tree.get_children())
                animal_list["values"] = AnimalName(found_username[0])

        def fill_treats_by_animal(x=None):
            #  after the vet chooses an animal fills the treatments tree
            treatments_tree.delete(*treatments_tree.get_children())
            found_username = Search(enter_username.get("1.0", "end-1c"))
            found_treats = get_treatments(found_username[0], animal_selected.get())
            i = 0
            for item in found_treats:
                treatments_tree.insert(parent='', index=i, iid=i, values=(item))
                i += 1

        self.columnconfigure(0, weight=1)
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

        animal_selected = tk.StringVar()
        ttk.Label(self, text="Select Animal: ").grid(padx=10, pady=20)
        animal_list = ttk.Combobox(self, textvariable=animal_selected)
        animal_list["state"] = "readonly"
        animal_list.grid(padx=10)
        animal_list.bind("<<ComboboxSelected>>", fill_treats_by_animal)  # event when animal is chosen

        ttk.Label(self, text="Treatments: ").grid(padx=10, pady=20)
        #  creating and setting the tree of the treatments
        treatments_tree = ttk.Treeview(self, height=15)
        treatments_tree['columns'] = ('Date', 'Time', 'Details')
        treatments_tree.column('#0', width=0, stretch="no")
        treatments_tree.column('Date', anchor="center", width=150, stretch="no")
        treatments_tree.column('Time', anchor="center", width=50, stretch="no")
        treatments_tree.column('Details', anchor="center", stretch="yes")
        treatments_tree.heading('#0', text='', anchor="center")
        treatments_tree.heading('Date', text='Date', anchor="center")
        treatments_tree.heading('Time', text='Time', anchor="center")
        treatments_tree.heading('Details', text='Details', anchor="center")
        treatments_tree.grid(sticky="EW")


class TodayAppointments(ttk.Frame):  # 4th tab - see today's appointments
    def __init__(self, container):
        super().__init__(container)

        def refresh_appoints():
            # after the refresh button is clicked, shows the appoints today
            today_appoints_tree.delete(*today_appoints_tree.get_children())
            i = 0
            today_appoints_list = retu_appoin(datetime.date.today())
            for item in today_appoints_list:
                today_appoints_tree.insert(parent='', index=i, iid=i, values=(item))
                i += 1

        self.columnconfigure(0, weight=1)
        ttk.Label(self, text="Appointments: ").grid(pady=30)
        #  creating and setting the tree of the appointments
        today_appoints_tree = ttk.Treeview(self, height=12)
        today_appoints_tree['columns'] = ('Hour', 'Animal Name')
        today_appoints_tree.column('#0', width=0, stretch="no")
        today_appoints_tree.column('Hour', anchor="center", width=150)
        today_appoints_tree.column('Animal Name', anchor="center", width=150)
        today_appoints_tree.heading('#0', text='', anchor="center")
        today_appoints_tree.heading('Hour', text='Hour', anchor="center")
        today_appoints_tree.heading('Animal Name', text='Animal Name', anchor="center")
        today_appoints_tree.grid()

        add_appoint_button = ttk.Button(self, text="Refresh", command=refresh_appoints)
        add_appoint_button.grid(ipadx=10, ipady=5, pady=30)


def veterinarian_main(id): # main veterinarian window setup
    # window setup
    vet_window = tk.Tk()
    vet_window.title("VetCare  -  Veterinarian")
    vet_window.resizable(False, False)
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

    # notebook creations
    tabs = ttk.Notebook(vet_window)
    # tabs.columnconfigure(0, weight=1)
    tabs.grid(sticky="EW")
    # tabs creations and adding to notebook
    info_of_animal_tab = AnimalInfo(tabs)
    tabs.add(info_of_animal_tab, text=" Animal Info ")
    new_treat_tab = NewTreatment(tabs)
    tabs.add(new_treat_tab, text=" New Treatment ")
    treat_record = TreatmentRecord(tabs)
    tabs.add(treat_record, text=" Treatment Record ")
    today_appoint = TodayAppointments(tabs)
    tabs.add(today_appoint, text=" Appointments Today  ")
    
    vet_window.mainloop()