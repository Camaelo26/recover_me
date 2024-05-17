from connection import create_connection
from view import view_appointment_details,view_appointments_by_date,view_appointments_by_department,view_appointments_by_patient_name
from update import update_appointment
from appointment import schedule_appointment,cancel_appointment
from department import add_department,list_departments,remove_department
from menu import doctor_menu,patient_menu
from register import register_user
from login import login_user
import os
import getpass

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#main
def Recover_me():

    host = 'localhost'
    username = 'root'
    password = 'yourpassword'
    database = 'database name'
    connection = create_connection(host, username, password, database)
    admin_access_code = "admins"
    current_user_id = None
    clear_screen()
    while True:
        print("======================================")
        print("  Welcome to RECOVER ME Appointment  ")
        print("======================================\n")
        print("1. Create New Account")
        print("2. Login")
        print("3. Admins")
        print("4. Exit\n")
        user_choice = input("Choose an option (1, 2, 3, 4): ")

        if user_choice == '1':
            # User input for account creation
            new_username = input("Enter username for new account: ")
            new_password = input("Enter password for new account: ")
            role = input("Enter role (Patient/Doctor) for new account: ").lower()
            
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            
            if role == 'patient':
                dob = input("Enter date of birth (YYYY-MM-DD): ")
                gender = input("Enter gender (Male/Female/Other): ")
                contact_number = input("Enter contact number: ")
                address = input("Enter address: ")
                email = input("Enter email: ")
                additional_info = (dob, gender, contact_number, address, email)
            elif role == 'doctor':
                department_id = input("Enter department ID: 1 for Cardio,2 for derma,3 for surgery, 4 for neuro, 5-for pediat,7-emergency ")
                contact_number = input("Enter contact number: ")
                email = input("Enter email: ")
                additional_info = (department_id, contact_number, email)

            register_user(connection, new_username, new_password, role, first_name, last_name, additional_info)
            print("Account created")
            clear_screen()
        elif user_choice == '2':
            # User input for login
            login_username = input("Enter your username to login: ")
            login_password = getpass.getpass("Enter your password to login: ")
            login_successful, role, user_id = login_user(connection, login_username, login_password)
            print(f"Login successful: {login_successful}")
            
            if login_successful:
                clear_screen()
                current_user_id = user_id
                print(f" Welcome, {login_username}.")
                if role == 'Doctor':
                    doctor_menu(connection, current_user_id)
                elif role == 'Patient':
                    patient_menu(connection, current_user_id)
            else:
                print("Login failed or user not found.")
        elif user_choice == '3':
         entered_code = input("Enter admin access code to proceed: ")
         if entered_code == admin_access_code:
          clear_screen()
          while True:
            print("\nAdmin Menu")
            print("1. Manage Appointments")
            print("2. Manage Departments")
            print("3. Return to Main Menu")

            admin_choice = input("Choose an action (1, 2,3): ")

            if admin_choice == '1':
             clear_screen()
             while True:
                print("\nAppointment Management")
                print("a. Schedule New Appointment")
                print("b. Update Appointment")
                print("c. Cancel Appointment")
                print("d. View Appointment Details")
                print("e. Return to Main Menu")
                appt_choice = input("Choose an action (a, b, c, d, e): ")

                if appt_choice == 'a':
                    clear_screen()
                    patient_id = input("Enter patient ID: ")
                    doctor_id = input("Enter doctor ID: ")
                    appointment_date = input("Enter appointment date (YYYY-MM-DD HH:MM:SS): ")
                    schedule_appointment(connection, patient_id, doctor_id, appointment_date)

                elif appt_choice == 'b':
                    clear_screen()
                    appointment_id = input("Enter appointment ID: ")
                    update_choice = input("Update (1) Date, (2) Doctor, or (3) Both? Enter 1, 2, or 3: ")
        
                    if update_choice == '1':
                        new_date = input("Enter new appointment date (YYYY-MM-DD HH:MM:SS): ")
                        update_appointment(connection, appointment_id, new_date=new_date)
                    elif update_choice == '2':
                        new_doctor_id = input("Enter new doctor ID: ")
                        update_appointment(connection, appointment_id, new_doctor_id=new_doctor_id)
                    elif update_choice == '3':
                        new_date = input("Enter new appointment date (YYYY-MM-DD HH:MM:SS): ")
                        new_doctor_id = input("Enter new doctor ID: ")
                        update_appointment(connection, appointment_id, new_doctor_id=new_doctor_id, new_date=new_date)


                elif appt_choice == 'c':
                    clear_screen()
                    appointment_id = input("Enter appointment ID to cancel: ")
                    cancel_appointment(connection, appointment_id)

                elif appt_choice == 'd':
                 clear_screen()
                 while True:
                    print("\nView Appointment Details")
                    print("1. View by Appointment ID")
                    print("2. View by Date")
                    print("3. View by Patient Name")
                    print("4. View by Department")
                    view_choice = input("Choose an option (1, 2, 3, 4): ")

                    if view_choice == '1':
                        appointment_id = input("Enter appointment ID to view details: ")
                        view_appointment_details(connection, appointment_id)
                    elif view_choice == '2':
                        appointment_date = input("Enter the date to view appointments (YYYY-MM-DD): ")
                        view_appointments_by_date(connection, appointment_date)
                    elif view_choice == '3':
                        patient_name = input("Enter the patient's name to search: ")
                        view_appointments_by_patient_name(connection, patient_name)
                    elif view_choice == '4':
                        department_name = input("Enter the department name to search: ")
                        view_appointments_by_department(connection, department_name)

                elif appt_choice == 'e':
                    break


            elif admin_choice == '2':  
             clear_screen()
             while True:
                print("\nDepartment Management")
                print("a. List Departments")
                print("b. Add Department")
                print("b. Remove Department")
                print("d. Return to Main Menu")
                dept_choice = input("Choose an action (a, b, c,d): ")

                if dept_choice == 'a':
                    list_departments(connection)
                elif dept_choice == 'b':
                    department_id = input("Enter the name of the department to be added: ")
                    add_department(connection, department_id)
                    print("department added")
                elif dept_choice == 'c':
                    department_id = input("Enter the ID of the department to remove: ")
                    remove_department(connection, department_id)
                    print("department removed")
                elif dept_choice == 'c':
                    break
                    
            elif admin_choice == '3':
             break  

         else:
          print("Incorrect access code. Access to Admin Menu denied.")
        elif user_choice == '4':
            print("Exiting the program.")
            clear_screen()
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    Recover_me()
