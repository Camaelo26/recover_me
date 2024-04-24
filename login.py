import hashlib
from mysql.connector import Error
def verify_password(stored_password, provided_password):
    salt = stored_password[:32]
    stored_key = stored_password[32:]
    new_key = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
    return stored_key == new_key

def login_user(connection, username, password):
    cursor = connection.cursor()
    try:
        # Fetch UserID, PasswordHash, and Role based on username
        cursor.execute("SELECT UserID, PasswordHash, Role FROM Users WHERE Username = %s", (username,))
        result = cursor.fetchone()
        if result and verify_password(result[1], password):
            user_id = result[0]
            role = result[2]

            if role == 'Doctor':
                # Fetch DoctorID for a doctor
                cursor.execute("SELECT DoctorID FROM Doctors WHERE UserID = %s", (user_id,))
                role_id = cursor.fetchone()[0]
            elif role == 'Patient':
                # Fetch PatientID for a patient
                cursor.execute("SELECT PatientID FROM Patients WHERE UserID = %s", (user_id,))
                role_id = cursor.fetchone()[0]
            else:
                role_id = user_id  # For other roles, use UserID as role_id

            return True, role, role_id
        else:
            return False, None, None
    except Error as e:
        print(f"Error logging in user: {e}")
    finally:
        cursor.close()
        
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
