import mysql.connector
from mysql.connector import Error
from executequery import execute_query

def update_appointment(connection, appointment_id, new_doctor_id=None, new_date=None):
    cursor = connection.cursor()
    try:
        if new_doctor_id and new_date:
            query = "UPDATE Appointments SET DoctorID = %s, AppointmentDate = %s WHERE AppointmentID = %s"
            cursor.execute(query, (new_doctor_id, new_date, appointment_id))
        elif new_doctor_id:
            query = "UPDATE Appointments SET DoctorID = %s WHERE AppointmentID = %s"
            cursor.execute(query, (new_doctor_id, appointment_id))
        elif new_date:
            query = "UPDATE Appointments SET AppointmentDate = %s WHERE AppointmentID = %s"
            cursor.execute(query, (new_date, appointment_id))
        else:
            print("No update information provided.")
            return

        connection.commit()
        print("Appointment updated successfully.")
    except Error as e:
        print(f"Error updating appointment: {e}")
    finally:
        cursor.close()
def update_doctor_info(connection, doctor_id, first_name=None, last_name=None, contact_number=None, email=None):
    cursor = connection.cursor()
    try:
        fields_to_update = []
        values = []

        if first_name:
            fields_to_update.append("FirstName = %s")
            values.append(first_name)
        if last_name:
            fields_to_update.append("LastName = %s")
            values.append(last_name)
        if contact_number:
            fields_to_update.append("ContactNumber = %s")
            values.append(contact_number)
        if email:
            fields_to_update.append("Email = %s")
            values.append(email)

        if fields_to_update:
            query = "UPDATE Doctors SET " + ", ".join(fields_to_update) + " WHERE DoctorID = %s"
            values.append(doctor_id)
            cursor.execute(query, tuple(values))
            connection.commit()
            print("Doctor information updated successfully.")
        else:
            print("No information provided to update.")

    except Error as e:
        print(f"Error updating doctor info: {e}")
    finally:
        cursor.close()

def update_patient_info(connection, patient_id, first_name=None, last_name=None, dob=None, gender=None, contact_number=None, address=None, email=None):
    cursor = connection.cursor()
    try:
        fields_to_update = []
        values = []

        if first_name:
            fields_to_update.append("FirstName = %s")
            values.append(first_name)
        if last_name:
            fields_to_update.append("LastName = %s")
            values.append(last_name)
        if dob:
            fields_to_update.append("DateOfBirth = %s")
            values.append(dob)
        if gender:
            fields_to_update.append("Gender = %s")
            values.append(gender)
        if contact_number:
            fields_to_update.append("ContactNumber = %s")
            values.append(contact_number)
        if address:
            fields_to_update.append("Address = %s")
            values.append(address)
        if email:
            fields_to_update.append("Email = %s")
            values.append(email)

        if fields_to_update:
            query = "UPDATE Patients SET " + ", ".join(fields_to_update) + " WHERE PatientID = %s"
            values.append(patient_id)
            cursor.execute(query, tuple(values))
            connection.commit()
            print("Patient information updated successfully.")
        else:
            print("No information provided to update.")

    except Error as e:
        print(f"Error updating patient info: {e}")
    finally:
        cursor.close()
def update_appointment_status(connection, appointment_id, new_status):
    query = "UPDATE Appointments SET Status = %s WHERE AppointmentID = %s"
    execute_query(connection, query, (new_status, appointment_id))
    print(f"Appointment ID {appointment_id} has been {new_status}.")