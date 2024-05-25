import mysql.connector
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='personal',
            user='root',
            password='Sistemas2002'
        )
        if connection.is_connected():
            print("Conexión exitosa")
    except Error as e:
        print(f"Error al conectarse a MySQL: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    connect()
