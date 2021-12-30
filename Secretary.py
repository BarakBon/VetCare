import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from window import *
from dbcontrol import *
from tkcalendar import Calendar
import datetime


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
                if flag is -2:
                    register_mistake.set("Wrong input")
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

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
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
            found_username = Search(enter_username.get("1.0","end-1c"))
            if not found_username:
                search_answer.set("No username found")
                firstname_info["state"] = "normal"
                firstname_info.delete("1.0", "end-1c")
                firstname_info["state"] = "disable"

                lastname_info["state"] = "normal"
                lastname_info.delete("1.0", "end-1c")
                lastname_info["state"] = "disable"

                phone_info["state"] = "normal"
                phone_info.delete("1.0", "end-1c")
                phone_info["state"] = "disable"

                email_info["state"] = "normal"
                email_info.delete("1.0", "end-1c")
                email_info["state"] = "disable"

                city_info["state"] = "normal"
                city_info.delete("1.0", "end-1c")
                city_info["state"] = "disable"

                usertype_info["state"] = "normal"
                usertype_info.delete("1.0", "end-1c")
                usertype_info["state"] = "disable"
                list_select.delete(0, tk.END)
                appoints_list_select.delete(0, tk.END)

                add_animal_button["state"] = "disabled"

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

                email_info["state"] = "normal"
                email_info.delete("1.0", "end-1c")
                email_info.insert(tk.END, found_username[5])
                email_info["state"] = "disable"

                city_info["state"] = "normal"
                city_info.delete("1.0", "end-1c")
                city_info.insert(tk.END, found_username[3])
                city_info["state"] = "disable"

                usertype_info["state"] = "normal"
                usertype_info.delete("1.0", "end-1c")
                usertype_info.insert(tk.END, found_username[6])
                usertype_info["state"] = "disable"

                if found_username[6] == "Customer":
                    add_animal_button["state"] = "normal"

                    nonlocal animal_list
                    animal_list = AnimalName(found_username[0])
                    list_select.delete(0, tk.END)
                    for item in animal_list:
                        list_select.insert(tk.END, item)

                    today = datetime.date.today()
                    nonlocal user_appoints_list
                    user_appoints_list = Customer_appointment(today, found_username[0])
                    appoints_list_select.delete(0, tk.END)
                    for item in user_appoints_list:
                        appoints_list_select.insert(tk.END, item[1] + " - " + str(item[2]) + " - " + item[3])

                else:
                    add_animal_button["state"] = "disabled"
                    list_select.delete(0, tk.END)
                    appoints_list_select.delete(0, tk.END)


        def add_animal():
            def add_animal_data():
                found_username = Search(enter_username.get("1.0", "end-1c"))
                add_animal_window.focus()
                print(animal_type_inserted.get())
                print(animal_name_inserted.get())
                if animal_type_inserted.get() is not "" and animal_name_inserted.get() is not "":
                    flag = newAnimal(found_username[0], animal_type_inserted.get(), animal_name_inserted.get())
                    print(flag)
                    if flag is not -2:
                        add_animal_window.destroy()
                        add_animal_button["state"] = "normal"
                add_animal_answer.set("Wrong Input")

            add_animal_window = tk.Tk()
            add_animal_window.title("Add  Animal")
            add_animal_window.resizable(False, False)
            set_window(add_animal_window)
            add_animal_button["state"] = "disabled"

            animal_name_inserted = tk.StringVar()
            animal_type_inserted = tk.StringVar()
            add_animal_answer = tk.StringVar()
            ttk.Label(add_animal_window, text="Animal name: ").grid(row=0, column=0, padx=10, pady=30)
            animal_name_entry = ttk.Entry(add_animal_window, width=20, textvariable=animal_name_inserted)
            animal_name_entry.grid(row=0, column=1, pady=10, padx=30)

            ttk.Label(add_animal_window, text="Animal Type: ").grid(row=1, column=0, padx=10)
            animal_type_entry = ttk.Entry(add_animal_window, width=20, textvariable=animal_type_inserted)
            animal_type_entry.grid(row=1, column=1, padx=10)

            ttk.Label(add_animal_window, textvariable=add_animal_answer, foreground="red").grid(row=3, column=1, pady=10, sticky="W")


            add_animal_data_button = ttk.Button(add_animal_window, text="Add Animal", command=add_animal_data)
            add_animal_data_button.grid(row=4, column=1, ipady=3, ipadx=10, sticky="W")
            add_animal_window.mainloop()


        user_select_frame = ttk.Frame(self)
        user_select_frame.grid(pady=20)
        search_answer = tk.StringVar()
        enter_username = tk.Text(user_select_frame, height=1, width=20)
        enter_username.grid(row=0, column=0, padx=30)
        enter_username.insert("1.0", "Enter username here")
        username_choose = ttk.Button(user_select_frame, text="Search", command=check_to_fill).grid(row=0, column=1)
        ttk.Label(user_select_frame, textvariable=search_answer, foreground="red").grid(row=1, column=0, padx=10, sticky="E")

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

        ttk.Label(user_output_frame, text="Email: ").grid(row=3, column=0, padx=20, pady=20)
        email_info = tk.Text(user_output_frame, state='disabled', height=1, width=20)
        email_info.grid(row=3, column=1, padx=30)

        ttk.Label(user_output_frame, text="City: ").grid(row=4, column=0, padx=20)
        city_info = tk.Text(user_output_frame, state='disabled', height=1, width=20)
        city_info.grid(row=4, column=1, padx=30)

        ttk.Label(user_output_frame, text="User Type: ").grid(row=5, column=0, padx=20, pady=20)
        usertype_info = tk.Text(user_output_frame, state='disabled', height=1, width=20)
        usertype_info.grid(row=5, column=1, padx=30)

        ttk.Label(user_output_frame, text="Animals: ").grid(row=6, column=0, padx=20, pady=20)
        animal_list = ()
        list_var = tk.StringVar(value=animal_list)
        list_select = tk.Listbox(user_output_frame, listvariable=list_var, height=len(animal_list))
        list_select.grid(row=6, column=1, padx=20, pady=20)

        ttk.Label(user_output_frame, text="Future Appointments: ").grid(row=7, column=0, padx=20, pady=30)
        user_appoints_list = ()
        appoints_list_var = tk.StringVar(value=user_appoints_list)
        appoints_list_select = tk.Listbox(user_output_frame, listvariable=appoints_list_var, height=len(user_appoints_list))
        appoints_list_select.grid(row=7, column=1, padx=20, pady=30)

        add_animal_button = ttk.Button(self, text="Add Animal", command=add_animal)
        add_animal_button["state"] = "disabled"
        add_animal_button.grid(ipady=3, ipadx=10, pady=20)


class ShowAppointments(ttk.Frame):  # third tab - show appointments info
    def __init__(self, container):
        super().__init__(container)

        def day_chose(x=None):  # working after the user press a day
            taken_appoints_tree.delete(*taken_appoints_tree.get_children())
            i = 0
            appoints_list = retu_appoin(cal.get_date())
            for item in appoints_list:
                taken_appoints_tree.insert(parent='', index=i, iid=i, values=(item))
                i += 1

        def delete_appoint():  # working after the button
            selected_appoint_to_del = taken_appoints_tree.focus()
            if selected_appoint_to_del:
                selected_to_del = taken_appoints_tree.item(selected_appoint_to_del, 'values')
                Queue_registration(None, None, cal.get_date(), selected_to_del[0])
                day_chose()


        ttk.Label(self, text="Select Date: ").grid(row=0, column=0, padx=10, pady=20)

        cal = Calendar(self, selectmode="day", firstweekday="sunday", mindate=datetime.date.today(), date_pattern='yyyy-mm-dd', weekendbackground="white")
        cal.grid(ipadx=80, ipady=30, padx=20, sticky="EW")
        cal.bind('<<CalendarSelected>>', day_chose)

        ttk.Label(self, text="Appointments: ").grid(pady=30)
        taken_appoints_tree = ttk.Treeview(self, height=4)
        taken_appoints_tree['columns'] = ('Hour', 'Animal Name')
        taken_appoints_tree.column('#0', width=0, stretch="no")
        taken_appoints_tree.column('Hour', anchor="center", width=150)
        taken_appoints_tree.column('Animal Name', anchor="center", width=150)
        taken_appoints_tree.heading('#0', text='', anchor="center")
        taken_appoints_tree.heading('Hour', text='Hour', anchor="center")
        taken_appoints_tree.heading('Animal Name', text='Animal Name', anchor="center")
        taken_appoints_tree.grid()


        add_appoint_button = ttk.Button(self, text="Delete", style="CustomButton.TButton", command=delete_appoint)
        add_appoint_button.grid(ipadx=10, ipady=5, pady=30)


class AddAnimal(ttk.Frame):  # 4th tab - add animal to customer
    def __init__(self, container):
        super().__init__(container)

        def check_to_fill(x=None):
            found_username = Search(enter_username.get("1.0","end-1c"))
            if not found_username:
                search_answer.set("No username found")

            else:
                search_answer.set("")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        user_select_frame = ttk.Frame(self)
        user_select_frame.grid(pady=20)
        search_answer = tk.StringVar()
        enter_username = tk.Text(user_select_frame, height=1, width=20)
        enter_username.grid(row=0, column=0, padx=30)
        enter_username.insert("1.0", "Enter username here")
        # ttk.Button(user_select_frame, text="Search", command=check_to_fill).grid(row=0, column=1)
        # ttk.Label(user_select_frame, textvariable=search_answer, foreground="red").grid(row=1, column=0, padx=10,
        #                                                                                 pady=5, sticky="E")
        ttk.Separator(self, orient='horizontal').grid(rowspan=2, sticky="EW")

        animal_name_inserted = tk.StringVar()
        animal_type_inserted = tk.StringVar()
        animal_output_frame = ttk.Frame(self)
        animal_output_frame.grid(pady=10)
        ttk.Label(animal_output_frame, text="Animal name: ").grid(row=0, column=0, padx=10, pady=20)
        animal_name_entry = ttk.Entry(animal_output_frame, width=20, textvariable=animal_name_inserted)
        animal_name_entry.grid(row=0, column=1, pady=10, padx=20)

        ttk.Label(animal_output_frame, text="Animal Type: ").grid(row=0, column=0, padx=10, pady=20)
        animal_type_entry = ttk.Entry(animal_output_frame, width=20, textvariable=animal_type_inserted)
        animal_type_entry.grid(row=0, column=1, pady=10, padx=20)

        # register_button = ttk.Button(self, text="Register", command=get_register_data)
        # register_button.grid(row=9, column=1, ipady=3, ipadx=10, pady=20, sticky="W")


def secretary_main(id):  # main secretary window setup
    # window setup
    secretary_window = tk.Tk()
    secretary_window.title("VetCare  -  Secretary")
    secretary_window.resizable(False, False)
    set_window(secretary_window)
    secretary_window.columnconfigure(0, weight=1)


    def s_logout():  # take care on the logout process
        if_logout_s_window = tk.Tk()
        if_logout_s_window.title("Warning")
        if_logout_s_window.resizable(False, False)
        set_window(if_logout_s_window)
        logout_button["state"] = "disable"
        ttk.Label(if_logout_s_window, text="Are you sure you want to logout? ").grid(row=0, column=0, padx=30,pady=10)
        ttk.Label(if_logout_s_window, text="All unsaved actions will be deleted. ", foreground="red").grid(row=1, column=0, padx=30, pady=5)
        logout_approve_frame = ttk.Frame(if_logout_s_window)
        logout_approve_frame.grid(row=2, column=0, pady=10)

        def yes_to_logout():  # if the user agreed to logout
            if_logout_s_window.destroy()
            secretary_window.destroy()

        def cancel_to_logout():  # if the user cancel the logout
            if_logout_s_window.destroy()
            logout_button["state"] = "normal"

        #  the buttons to agree or not to logout
        ttk.Button(logout_approve_frame, text="Yes", command=yes_to_logout).grid(row=0, column=0, ipadx=5, ipady=2, padx=5)
        ttk.Button(logout_approve_frame, text="Cancel", command=cancel_to_logout).grid(row=0, column=1, ipadx=5,ipady=2, padx=5)
        if_logout_s_window.protocol("WM_DELETE_WINDOW", cancel_to_logout)


    def s_no_exit():
        pass

    # custom style for the logout button
    style = ttk.Style(secretary_window)
    style.map("CustomButton.TButton", foreground=[("!pressed", "red")], backround=[("!pressed", "red")])

    # logged in top bar title and logout button in frame
    logged_bar_frame = ttk.Frame(secretary_window).grid(sticky="EW")
    ttk.Label(logged_bar_frame, text=("Hello,   "+ UserID_to_First_Name(id))).grid(row=0, column=0, padx=20, pady=10, sticky="W")
    logout_button = ttk.Button(logged_bar_frame, text="Log Out", style="CustomButton.TButton",command=s_logout)
    logout_button.grid(row=0, column=0, padx=10, pady=10, sticky="E")
    secretary_window.protocol("WM_DELETE_WINDOW", s_no_exit)

    # tabs creations
    tabs = ttk.Notebook(secretary_window)
    # tabs.columnconfigure(0, weight=1)
    tabs.grid(sticky="EW")
    register_new_user_tab = SignupTab(tabs)
    tabs.add(register_new_user_tab, text=" Signup ")
    info_of_user = UserInfo(tabs)
    tabs.add(info_of_user, text=" User Info ")
    show_appoints = ShowAppointments(tabs)
    tabs.add(show_appoints, text=" Appointments ")
    add_animal = AddAnimal(tabs)
    tabs.add(add_animal, text=" Add Animal ")


    secretary_window.mainloop()



