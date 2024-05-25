import mysql.connector
from mysql.connector import Error

def connect():
    """ Connect to MySQL database and perform queries """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='personal',
            user='root',
            password='Sistemas2002'
        )
        if connection.is_connected():
            print("Conexión exitosa")
            query_data(connection)
    except Error as e:
        print(f"Error al conectarse a MySQL: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def query_data(connection):
    """ Query data from the personas table """
    try:
        cursor = connection.cursor()
        query = "SELECT id, nombre, ciudad FROM personas WHERE ciudad = 'Cuenca' "
        cursor.execute(query)
        results = cursor.fetchall()
        print("Datos recuperados:")
        for row in results:
            print(row)
    except Error as e:
        print(f"Error al consultar datos: {e}")
    finally:
        cursor.close()

if __name__ == "__main__":
    connect()
