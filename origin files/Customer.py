import time
import tkinter as tk
from tkinter import ttk
from window import *
from dbcontrol import *
from tkcalendar import Calendar
import datetime

class MakeAppointment(ttk.Frame):  # first tab - make appointment by the user
    def __init__(self, container, *args):
        super().__init__(container, *args)

        def day_chose(x=None):
            # working after the user chooses a day and fills the free times
            free_times = Show_appointment(cal.get_date())
            free_time_combo["values"] = free_times

        def create_appoint():
            # working after the button and creates the new appoint
            def appoint_created_ok():
                appoint_created_alert.destroy()
                add_appoint_button["state"] = "normal"
                day_chose()

            if cal.get_date() is "" or time_selected.get() is "" or animal_selected.get() is "":
                appoint_mistake.set("Select all options")
            else:
                #  only if he chooses all the options he creates an appointment
                Queue_registration(animal_selected.get(), cust_id, cal.get_date(), time_selected.get())
                appoint_mistake.set("")
                #  creates and pops a window that says the appoint has been created
                appoint_created_alert = tk.Tk()
                appoint_created_alert.title("Success")
                appoint_created_alert.resizable(False, False)
                set_window(appoint_created_alert)
                add_appoint_button["state"] = "disabled"
                day_chose()
                ttk.Label(appoint_created_alert, text="Appointment created successfully. ", foreground="green").grid(
                    row=0, column=0,
                    padx=30, pady=20)
                ttk.Button(appoint_created_alert, text="OK", command=appoint_created_ok).grid(ipadx=10, ipady=5,
                                                                                              pady=10)
                appoint_created_alert.protocol("WM_DELETE_WINDOW", appoint_created_ok)


        time_selected = tk.StringVar()
        animal_selected = tk.StringVar()
        appoint_mistake = tk.StringVar()
        free_times = ()

        ttk.Label(self, text="Select Date: ").grid(row=0, column=0, padx=10, pady=20)

        cal = Calendar(self, selectmode="day", firstweekday="sunday", mindate=datetime.date.today(), date_pattern='yyyy-mm-dd', weekendbackground="white")
        cal.grid(ipadx=80, ipady=30, padx=20, sticky="EW")
        cal.bind('<<CalendarSelected>>', day_chose)

        ttk.Label(self, text="Select Hour: ").grid(pady=20)
        free_time_combo = ttk.Combobox(self, textvariable=time_selected)
        free_time_combo["state"] = "readonly"
        free_time_combo.grid()

        ttk.Label(self, text="Select Animal: ").grid(pady=30)
        animal_select_list = ttk.Combobox(self, textvariable=animal_selected)
        animal_select_list["values"] = AnimalName(cust_id)
        animal_select_list["state"] = "readonly"
        animal_select_list.grid()

        ttk.Label(self, textvariable=appoint_mistake, foreground="red").grid(pady=30)

        add_appoint_button = ttk.Button(self, text="Choose", command=create_appoint)
        add_appoint_button.grid(ipadx=10, ipady=5, pady=10)


class AnimalInfo(ttk.Frame):  # second tab - see the animals info and appointments
    def __init__(self, container, *args):
        super().__init__(container, *args)

        def fill_appoints_by_animal(x=None):
            #  fills the info and appoints of the animal chosen
            found_animal_info = animal_details(cust_id, animal_selected.get())
            animal_name_info["state"] = "normal"
            animal_name_info.delete("1.0", "end-1c")
            animal_name_info.insert(tk.END, found_animal_info[1])
            animal_name_info["state"] = "disable"

            animal_type_info["state"] = "normal"
            animal_type_info.delete("1.0", "end-1c")
            animal_type_info.insert(tk.END, found_animal_info[0])
            animal_type_info["state"] = "disable"

            today = datetime.date.today()
            user_appoints_list = Animal_appointment(today, cust_id, animal_selected.get())
            animal_appoints_tree.delete(*animal_appoints_tree.get_children())
            i = 0
            for item in user_appoints_list:
                animal_appoints_tree.insert(parent='', index=i, iid=i, values=(item[2], item[3]))
                i += 1

        def delete_appoint():
            # working after the button and deleting the chosen appoint
            selected_appoint_to_del = animal_appoints_tree.focus()
            if selected_appoint_to_del:
                selected_to_del = animal_appoints_tree.item(selected_appoint_to_del, 'values')
                Queue_registration(None, None, selected_to_del[1], selected_to_del[0])
                fill_appoints_by_animal()

        self.columnconfigure(0, weight=1)
        animal_selected = tk.StringVar()
        ttk.Label(self, text="Select Animal: ").grid(pady=30)
        animal_select_list = ttk.Combobox(self, textvariable=animal_selected)
        animal_select_list["values"] = AnimalName(cust_id)
        animal_select_list["state"] = "readonly"
        animal_select_list.grid()
        animal_select_list.bind("<<ComboboxSelected>>", fill_appoints_by_animal)  # event of the chosen animal

        animal_output_frame = ttk.Frame(self)
        animal_output_frame.grid(pady=20)
        ttk.Label(animal_output_frame, text="Animal Name: ").grid(row=0, column=0, padx=20, pady=20)
        animal_name_info = tk.Text(animal_output_frame, state='disabled', height=1, width=20)
        animal_name_info.grid(row=0, column=1, padx=30)

        ttk.Label(animal_output_frame, text="Animal Type: ").grid(row=1, column=0, padx=20)
        animal_type_info = tk.Text(animal_output_frame, state='disabled', height=1, width=20)
        animal_type_info.grid(row=1, column=1, padx=30)

        ttk.Label(self, text="Appointments: ").grid(pady=30)
        #  creating and setting up the appointments tree
        animal_appoints_tree = ttk.Treeview(self, height=12)
        animal_appoints_tree['columns'] = ('Hour', 'Animal Name')
        animal_appoints_tree.column('#0', width=0, stretch="no")
        animal_appoints_tree.column('Hour', anchor="center", width=150)
        animal_appoints_tree.column('Animal Name', anchor="center", width=150)
        animal_appoints_tree.heading('#0', text='', anchor="center")
        animal_appoints_tree.heading('Hour', text='Hour', anchor="center")
        animal_appoints_tree.heading('Animal Name', text='Animal Name', anchor="center")
        animal_appoints_tree.grid()

        add_appoint_button = ttk.Button(self, text="Delete", style="CustomButton.TButton", command=delete_appoint)
        add_appoint_button.grid(ipadx=10, ipady=5, pady=30)


class AnimalMedicalRec(ttk.Frame):  # third tab - see the animals medical record
    def __init__(self, container, *args):
        super().__init__(container, *args)

        def fill_treats_by_animal(x=None):
            #  fills the treatments of the chosen animal
            treatments_tree.delete(*treatments_tree.get_children())
            found_treats = get_treatments(cust_id, animal_selected.get())
            i = 0
            for item in found_treats:
                treatments_tree.insert(parent='', index=i, iid=i, values=(item))
                i += 1

        self.columnconfigure(0, weight=1)
        animal_selected = tk.StringVar()
        ttk.Label(self, text="Select Animal: ").grid(padx=10, pady=20)
        animal_list = ttk.Combobox(self, textvariable=animal_selected)
        animal_list["state"] = "readonly"
        animal_list.grid(padx=10)
        animal_list.bind("<<ComboboxSelected>>", fill_treats_by_animal)
        animal_list["values"] = AnimalName(cust_id)

        ttk.Label(self, text="Treatments: ").grid(padx=10, pady=20)
        #  creating and setting up the treatments tree
        treatments_tree = ttk.Treeview(self, height=20)
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


cust_id = None
def customer_main(c_id):  # main customer window setup
    global cust_id
    cust_id = c_id
    # window setup
    customer_window = tk.Tk()
    customer_window.title("VetCare  -  Customer")
    customer_window.resizable(False, False)
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
        if_logout_c_window.protocol("WM_DELETE_WINDOW", cancel_to_logout)


    def c_no_exit():
        pass

    # logged in top bar title and logout button in frame
    logged_bar_frame = ttk.Frame(customer_window).grid(sticky="EW")
    ttk.Label(logged_bar_frame, text=("Hello,   " + UserID_to_First_Name(c_id))).grid(row=0, column=0, padx=20, pady=10, sticky="W")
    logout_button = ttk.Button(logged_bar_frame, text="Log Out", style="CustomButton.TButton", command=c_logout)
    logout_button.grid(row=0, column=0, padx=10, pady=10, sticky="E")
    customer_window.protocol("WM_DELETE_WINDOW", c_no_exit)

    # notebook creations
    tabs = ttk.Notebook(customer_window)
    # tabs.columnconfigure(0, weight=1)
    tabs.grid(sticky="EW")
    # tabs creations and adding to notebook
    register_new_user_tab = MakeAppointment(tabs)
    tabs.add(register_new_user_tab, text=" Make Appointment ")
    animal_info_tab = AnimalInfo(tabs)
    tabs.add(animal_info_tab, text=" Animal Details ")
    animal_med_rec = AnimalMedicalRec(tabs)
    tabs.add(animal_med_rec, text=" Medical Record ")

    customer_window.mainloop()

