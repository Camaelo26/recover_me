import hashlib
from executequery import execute_query
import os


def hash_password(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + key

def register_user(connection, username, password, role, first_name, last_name, additional_info):
    # Step 1: Register user account
    hashed_password = hash_password(password)
    user_query = "INSERT INTO Users (Username, PasswordHash, Role) VALUES (%s, %s, %s)"
    execute_query(connection, user_query, (username, hashed_password, role))

    # Step 2: Fetch the newly created UserID
    cursor = connection.cursor()
    cursor.execute("SELECT UserID FROM Users WHERE Username = %s", (username,))
    user_id = cursor.fetchone()[0]

    # Step 3: Store role-specific information
    if role.lower() == 'patient':
        # Assume additional_info is a tuple (dob, gender, contact_number, address, email)
        patient_query = """
        INSERT INTO Patients (UserID, FirstName, LastName, DateOfBirth, Gender, ContactNumber, Address, Email) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        execute_query(connection, patient_query, (user_id, first_name, last_name) + additional_info)
    elif role.lower() == 'doctor':
        # Assume additional_info is a tuple (department_id, contact_number, email)
        doctor_query = """
        INSERT INTO Doctors (UserID, FirstName, LastName, DepartmentID, ContactNumber, Email) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        execute_query(connection, doctor_query, (user_id, first_name, last_name) + additional_info)

    cursor.close()