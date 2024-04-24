from executequery import execute_query
from mysql.connector import Error
def add_patient(connection, user_id, first_name, last_name, dob, gender, contact_number, address, email):
    query = """
    INSERT INTO Patients (UserID, FirstName, LastName, DateOfBirth, Gender, ContactNumber, Address, Email) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    execute_query(connection, query, (user_id, first_name, last_name, dob, gender, contact_number, address, email))

def update_patient(connection, patient_id, first_name, last_name, dob, gender, contact_number, address, email):
    query = """
    UPDATE Patients 
    SET FirstName = %s, LastName = %s, DateOfBirth = %s, Gender = %s, ContactNumber = %s, Address = %s, Email = %s 
    WHERE PatientID = %s
    """
    execute_query(connection, query, (first_name, last_name, dob, gender, contact_number, address, email, patient_id))

def view_patient_details(connection, patient_id):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM Patients WHERE PatientID = %s", (patient_id,))
        result = cursor.fetchone()
        print("Patient Details:", result)
    except Error as e:
        print(f"Error reading patient data: {e}")
    finally:
        cursor.close()