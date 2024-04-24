import mysql.connector
from mysql.connector import Error
from executequery import execute_query


def add_department(connection, department_name):
    query = "INSERT INTO Departments (DepartmentName) VALUES (%s)"
    execute_query(connection, query, (department_name,))


def list_departments(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT DepartmentID, DepartmentName FROM Departments")
        results = cursor.fetchall()
        if results:
            print("List of Departments:")
            for dept in results:
                print(f"ID: {dept[0]}, Name: {dept[1]}")
        else:
            print("No departments found.")
    except Error as e:
        print(f"Error fetching departments: {e}")
    finally:
        cursor.close()

def remove_department(connection, department_id):
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM Departments WHERE DepartmentID = %s", (department_id,))
        connection.commit()
        print("Department removed successfully.")
    except Error as e:
        print(f"Error removing department: {e}")
    finally:
        cursor.close()

def list_doctors_by_department(connection, department_name):
    cursor = connection.cursor()
    try:
        query = """
        SELECT Doctors.DoctorID, Doctors.FirstName, Doctors.LastName 
        FROM Doctors
        JOIN Departments ON Doctors.DepartmentID = Departments.DepartmentID
        WHERE Departments.DepartmentName = %s
        """
        cursor.execute(query, (department_name,))
        results = cursor.fetchall()

        if results:
            print(f"Doctors in the {department_name} Department:")
            for doctor in results:
                print(f"ID: {doctor[0]}, Name: {doctor[1]} {doctor[2]}")
        else:
            print(f"No doctors found in the {department_name} Department.")
    except Error as e:
        print(f"Error fetching doctors: {e}")
    finally:
        cursor.close()