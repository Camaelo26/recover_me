from appointment import review_appointments,request_appointment,view_my_appointments,change_appointment_time,request_new_appointment_time,cancel_appointment_by_patient
from department import list_doctors_by_department
from update import update_doctor_info,update_patient_info
from view import view_scheduled_patient_info
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def doctor_menu(connection, doctor_id):
    while True:
        print("\nDoctor Menu")
        print("1. Review Pending Appointments and others")
        print("2. Update My Information")
        print("3. View Scheduled Appointments and Patient Information")
        print("4. Return to Main Menu")
        choice = input("Choose an action (1, 2, 3,4): ")

        if choice == '1':
            review_appointments(connection, doctor_id)
        elif choice == '2':
            # Get new information from doctor
            first_name = input("Enter new first name or press enter to skip: ")
            last_name = input("Enter new last name or press enter to skip: ")
            contact_number = input("Enter new contact number or press enter to skip: ")
            email = input("Enter new email or press enter to skip: ")

            update_doctor_info(connection, doctor_id, first_name, last_name, contact_number, email)
        elif choice == '3':
            view_scheduled_patient_info(connection, doctor_id)
        elif choice == '4':
            clear_screen()
            break
def patient_menu(connection, patient_id):
    while True:
        print("\nPatient Menu")
        print("1. Request an Appointment")
        print("2. View My Appointments")
        print("3. Update My Information")
        print("4. Change Appointment Time")
        print("5. Request New Time for Appointment")
        print("6. Cancel Appointment")
        print("7. Return to Main Menu")
        choice = input("Choose an action (1, 2, 3, 4, 5, 6, 7): ")

        if choice == '1':
            department_name = input("Enter the department name for the appointment ( Cardiology , dermatology, surgery, neurology, pediathry,emergency): ")
            list_doctors_by_department(connection, department_name)
            doctor_id = input("Enter the ID of the doctor you want to make an appointment with: ")
            desired_date = input("Enter the desired date for your appointment (YYYY-MM-DD HH:MM:SS): ")
            request_appointment(connection, patient_id, doctor_id, desired_date)
        elif choice == '2':
            
            view_my_appointments(connection, patient_id)
        elif choice == '3':
            # Get new information from patient
            first_name = input("Enter new first name or press enter to skip: ")
            last_name = input("Enter new last name or press enter to skip: ")
            dob = input("Enter new date of birth (YYYY-MM-DD) or press enter to skip: ")
            gender = input("Enter new gender or press enter to skip: ")
            contact_number = input("Enter new contact number or press enter to skip: ")
            address = input("Enter new address or press enter to skip: ")
            email = input("Enter new email or press enter to skip: ")
            update_patient_info(connection, patient_id, first_name, last_name, dob, gender, contact_number, address, email)
        elif choice == '4':
            appointment_id = input("Enter your appointment ID to change time: ")
            new_date = input("Enter the new date and time for your appointment (YYYY-MM-DD HH:MM:SS): ")
            change_appointment_time(connection, patient_id, appointment_id, new_date)
        elif choice == '5':
            appointment_id = input("Enter your appointment ID to request a new time: ")
            requested_date = input("Enter the requested new date and time (YYYY-MM-DD HH:MM:SS): ")
            request_new_appointment_time(connection, patient_id, appointment_id, requested_date)
        elif choice == '6':
            appointment_id = input("Enter your appointment ID to cancel: ")
            cancel_appointment_by_patient(connection, patient_id, appointment_id)
        elif choice == '7':
            clear_screen()
            break