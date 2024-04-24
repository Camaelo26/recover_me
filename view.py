from mysql.connector import Error
from executequery import execute_query



def view_appointment_details(connection, appointment_id):
    cursor = connection.cursor()
    try:
        query = """
        SELECT 
            Appointments.AppointmentID, 
            Appointments.AppointmentDate, 
            Appointments.Status, 
            Patients.FirstName AS PatientFirstName, 
            Patients.LastName AS PatientLastName,
            Doctors.FirstName AS DoctorFirstName, 
            Doctors.LastName AS DoctorLastName
        FROM 
            Appointments
        JOIN Patients ON Appointments.PatientID = Patients.PatientID
        JOIN Doctors ON Appointments.DoctorID = Doctors.DoctorID
        WHERE 
            Appointments.AppointmentID = %s
        """
        cursor.execute(query, (appointment_id,))
        result = cursor.fetchone()
        
        if result:
            print("Appointment Details:")
            print(f"Appointment ID: {result[0]}")
            print(f"Date: {result[1]}")
            print(f"Status: {result[2]}")
            print(f"Patient Name: {result[3]} {result[4]}")
            print(f"Doctor Name: {result[5]} {result[6]}")
        else:
            print("No appointment found with the given ID.")

    except Error as e:
        print(f"Error reading appointment data: {e}")
    finally:
        cursor.close()


def view_appointments_by_date(connection, appointment_date):
    cursor = connection.cursor()
    try:
        query = """
        SELECT 
            Doctors.FirstName AS DoctorFirstName, 
            Doctors.LastName AS DoctorLastName, 
            Patients.FirstName AS PatientFirstName, 
            Patients.LastName AS PatientLastName, 
            Appointments.AppointmentDate
        FROM 
            Appointments
        JOIN Patients ON Appointments.PatientID = Patients.PatientID
        JOIN Doctors ON Appointments.DoctorID = Doctors.DoctorID
        WHERE 
            DATE(Appointments.AppointmentDate) = %s
        """
        cursor.execute(query, (appointment_date,))
        results = cursor.fetchall()

        if results:
            print(f"Appointments for {appointment_date}:")
            for result in results:
                print(f"Time: {result[4]}, Doctor: {result[0]} {result[1]}, Patient: {result[2]} {result[3]}")
        else:
            print("No appointments found for the given date.")

    except Error as e:
        print(f"Error reading appointments data: {e}")
    finally:
        cursor.close()
def view_appointments_by_patient_name(connection, patient_name):
    cursor = connection.cursor()
    try:
        query = """
        SELECT Appointments.AppointmentID, Doctors.FirstName AS DoctorFirstName, Doctors.LastName AS DoctorLastName, Appointments.AppointmentDate, Appointments.Status
        FROM Appointments
        JOIN Patients ON Appointments.PatientID = Patients.PatientID
        JOIN Doctors ON Appointments.DoctorID = Doctors.DoctorID
        WHERE Patients.FirstName LIKE %s OR Patients.LastName LIKE %s
        """
        cursor.execute(query, (patient_name + '%', patient_name + '%'))
        results = cursor.fetchall()

        if results:
            print("Appointments for patient:", patient_name)
            for appt in results:
                print(f"ID: {appt[0]}, Doctor: {appt[1]} {appt[2]}, Date: {appt[3]}, Status: {appt[4]}")
        else:
            print(f"No appointments found for patient with name: {patient_name}")
    except Error as e:
        print(f"Error fetching appointments: {e}")
    finally:
        cursor.close()
def view_appointments_by_department(connection, department_name):
    cursor = connection.cursor()
    try:
        query = """
        SELECT Appointments.AppointmentID, Patients.FirstName AS PatientFirstName, Patients.LastName AS PatientLastName, Appointments.AppointmentDate, Appointments.Status
        FROM Appointments
        JOIN Doctors ON Appointments.DoctorID = Doctors.DoctorID
        JOIN Departments ON Doctors.DepartmentID = Departments.DepartmentID
        JOIN Patients ON Appointments.PatientID = Patients.PatientID
        WHERE Departments.DepartmentName = %s
        """
        cursor.execute(query, (department_name,))
        results = cursor.fetchall()

        if results:
            print(f"Appointments in {department_name} department:")
            for appt in results:
                print(f"ID: {appt[0]}, Patient: {appt[1]} {appt[2]}, Date: {appt[3]}, Status: {appt[4]}")
        else:
            print(f"No appointments found in {department_name} department.")
    except Error as e:
        print(f"Error fetching appointments: {e}")
    finally:
        cursor.close()


def view_scheduled_patient_info(connection, doctor_id):
    cursor = connection.cursor()
    try:
        query = """
        SELECT 
            Patients.PatientID, 
            Patients.FirstName, 
            Patients.LastName, 
            Patients.DateOfBirth, 
            Patients.Gender, 
            Patients.ContactNumber, 
            Patients.Address, 
            Patients.Email,
            Appointments.AppointmentDate
        FROM 
            Appointments
        JOIN 
            Patients ON Appointments.PatientID = Patients.PatientID
        WHERE 
            Appointments.DoctorID = %s AND Appointments.Status = 'Scheduled'
        ORDER BY 
            Appointments.AppointmentDate
        """
        cursor.execute(query, (doctor_id,))
        results = cursor.fetchall()

        if results:
            print("Scheduled Appointments and Patient Information:")
            for appt in results:
                print(f"\nAppointment Date: {appt[8]}")
                print(f"Patient ID: {appt[0]}, Name: {appt[1]} {appt[2]}, Date of Birth: {appt[3]}, Gender: {appt[4]}")
                print(f"Contact Number: {appt[5]}, Address: {appt[6]}, Email: {appt[7]}")
        else:
            print("No scheduled appointments found.")
    except Error as e:
        print(f"Error fetching patient information: {e}")
    finally:
        cursor.close()
