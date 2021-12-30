import time
import tkinter as tk
from tkinter import ttk
from window import *
from dbcontrol import *
from tkcalendar import Calendar
import datetime

class MakeAppointment(ttk.Frame):  # make appointment by the user
    def __init__(self, container, *args):
        super().__init__(container, *args)

        def day_chose(x=None):  # working after the user press a day
            free_times = Show_appointment(cal.get_date())
            free_time_combo["values"] = free_times

        def create_appoint():  # working after the button
            def appoint_created_ok():
                appoint_created_alert.destroy()
                add_appoint_button["state"] = "normal"
                day_chose()

            if cal.get_date() is "" or time_selected.get() is "" or animal_selected.get() is "":
                appoint_mistake.set("Select all options")
            else:
                Queue_registration(animal_selected.get(), cust_id, cal.get_date(), time_selected.get())
                appoint_mistake.set("")
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


class AnimalAppointments(ttk.Frame):  # see the animals appointment
    def __init__(self, container, *args):
        super().__init__(container, *args)

        def fill_appoints_by_animal(x=None):
            today = datetime.date.today()
            nonlocal user_appoints_list
            user_appoints_list = Animal_appointment(today, cust_id, animal_selected.get())
            appoints_list_select.delete(0, tk.END)
            for item in user_appoints_list:
                appoints_list_select.insert(tk.END, str(item[2]) + "  -  " + item[3])

        self.columnconfigure(0, weight=1)
        animal_selected = tk.StringVar()
        ttk.Label(self, text="Select Animal: ").grid(pady=30)
        animal_select_list = ttk.Combobox(self, textvariable=animal_selected)
        animal_select_list["values"] = AnimalName(cust_id)
        animal_select_list["state"] = "readonly"
        animal_select_list.grid()
        animal_select_list.bind("<<ComboboxSelected>>", fill_appoints_by_animal)

        ttk.Label(self, text="Future Appointments: ").grid(padx=20, pady=40)
        user_appoints_list = ()
        appoints_list_var = tk.StringVar(value=user_appoints_list)
        appoints_list_select = tk.Listbox(self, listvariable=appoints_list_var,
                                          height=len(user_appoints_list))
        appoints_list_select.grid(padx=20)


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
    logout_button = ttk.Button(logged_bar_frame, text="Log Out", style="CustomButton.TButton",command=c_logout)
    logout_button.grid(row=0, column=0, padx=10, pady=10, sticky="E")
    customer_window.protocol("WM_DELETE_WINDOW", c_no_exit)

    # tabs creations
    tabs = ttk.Notebook(customer_window)
    # tabs.columnconfigure(0, weight=1)
    tabs.grid(sticky="EW")
    register_new_user_tab = MakeAppointment(tabs)
    tabs.add(register_new_user_tab, text=" Make Appointment ")
    animal_appoints_tab = AnimalAppointments(tabs)
    tabs.add(animal_appoints_tab, text=" Animal Appointment ")

    customer_window.mainloop()

