
from mysql.connector import Error
from executequery import execute_query
from update import update_appointment_status

def schedule_appointment(connection, patient_id, doctor_id, appointment_date):
    query = """
    INSERT INTO Appointments (PatientID, DoctorID, AppointmentDate, Status) 
    VALUES (%s, %s, %s, 'Scheduled')
    """
    execute_query(connection, query, (patient_id, doctor_id, appointment_date))

def cancel_appointment(connection, appointment_id):
    query = "UPDATE Appointments SET Status = 'Cancelled' WHERE AppointmentID = %s"
    execute_query(connection, query, (appointment_id,))


def request_appointment(connection, patient_id, doctor_id, desired_datetime):
    query = """
    INSERT INTO Appointments (PatientID, DoctorID, AppointmentDate, Status) 
    VALUES (%s, %s, %s, 'Pending')
    """
    execute_query(connection, query, (patient_id, doctor_id, desired_datetime))
    print("Appointment request submitted. Awaiting doctor's approval.")


def view_my_appointments(connection, patient_id):
    cursor = connection.cursor()
    try:
        query = """
        SELECT 
            Appointments.AppointmentID, 
            Doctors.FirstName AS DoctorFirstName, 
            Doctors.LastName AS DoctorLastName, 
            Departments.DepartmentName,
            Appointments.AppointmentDate,
            Appointments.Status
        FROM 
            Appointments
        JOIN Doctors ON Appointments.DoctorID = Doctors.DoctorID
        JOIN Departments ON Doctors.DepartmentID = Departments.DepartmentID
        WHERE 
            Appointments.PatientID = %s
        ORDER BY 
            Appointments.AppointmentDate DESC
        """
        cursor.execute(query, (patient_id,))
        results = cursor.fetchall()

        if results:
            print("\nYour Appointments:")
            for appointment in results:
                print(f"ID: {appointment[0]}, Doctor: {appointment[1]} {appointment[2]}, Department: {appointment[3]}, Date: {appointment[4]}, Status: {appointment[5]}")
        else:
            print("You have no appointments scheduled.")
    except Error as e:
        print(f"Error fetching appointments: {e}")
    finally:
        cursor.close()   
def change_appointment_time(connection, patient_id, appointment_id, new_date):
    cursor = connection.cursor()
    try:
        # Check if the appointment is pending and belongs to the patient
        cursor.execute("SELECT Status FROM Appointments WHERE AppointmentID = %s AND PatientID = %s", (appointment_id, patient_id))
        result = cursor.fetchone()
        if result and result[0] == 'Pending':
            query = "UPDATE Appointments SET AppointmentDate = %s, Status = 'Pending' WHERE AppointmentID = %s"
            cursor.execute(query, (new_date, appointment_id))
            connection.commit()
            print("Appointment time changed successfully.")
        else:
            print("Only pending appointments can be changed.")
    except Error as e:
        print(f"Error updating appointment: {e}")
    finally:
        cursor.close()
def request_new_appointment_time(connection, patient_id, appointment_id, requested_date):
    cursor = connection.cursor()
    try:
        # Check if the appointment belongs to the patient
        cursor.execute("SELECT AppointmentID FROM Appointments WHERE AppointmentID = %s AND PatientID = %s", (appointment_id, patient_id))
        if cursor.fetchone():
            query = "UPDATE Appointments SET AppointmentDate = %s, Status = 'Pending' WHERE AppointmentID = %s"
            cursor.execute(query, (requested_date, appointment_id))
            connection.commit()
            print("New appointment time requested.")
        else:
            print("Appointment not found.")
    except Error as e:
        print(f"Error requesting new appointment time: {e}")
    finally:
        cursor.close()
def cancel_appointment_by_patient(connection, patient_id, appointment_id):
    cursor = connection.cursor()
    try:
        query = "UPDATE Appointments SET Status = 'Cancelled' WHERE AppointmentID = %s AND PatientID = %s"
        cursor.execute(query, (appointment_id, patient_id))
        connection.commit()
        print("Appointment cancelled successfully.")
    except Error as e:
        print(f"Error cancelling appointment: {e}")
    finally:
        cursor.close()


def review_appointments(connection, doctor_id):
    cursor = connection.cursor()
    try:
        query = """
        SELECT AppointmentID, Patients.FirstName, Patients.LastName, AppointmentDate, Status
        FROM Appointments
        JOIN Patients ON Appointments.PatientID = Patients.PatientID
        WHERE DoctorID = %s
        ORDER BY AppointmentDate
        """
        cursor.execute(query, (doctor_id,))
        results = cursor.fetchall()

        if results:
            for appt in results:
                print(f"ID: {appt[0]}, Patient: {appt[1]} {appt[2]}, Date: {appt[3]}, Status: {appt[4]}")
                if appt[4] == 'Pending':
                    response = input(f"Accept appointment ID {appt[0]}? (y/n): ")
                    update_status = "Scheduled" if response.lower() == 'y' else "Cancelled"
                    update_appointment_status(connection, appt[0], update_status)
        else:
            print("No appointments found for this doctor.")
    except Error as e:
        print(f"Error fetching appointments: {e}")
    finally:
        cursor.close()