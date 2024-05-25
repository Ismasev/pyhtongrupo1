import mysql.connector
from mysql.connector import Error

def connect():
    """ Connect to MySQL database and insert data """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='personal',
            user='root',
            password='Sistemas2002'
        )
        if connection.is_connected():
            print("Conexión exitosa")
            insert_multiple_data(connection)
    except Error as e:
        print(f"Error al conectarse a MySQL: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def insert_multiple_data(connection):
    """ Insert multiple rows into the personas table """
    try:
        cursor = connection.cursor()
        query = """INSERT INTO personas (nombre, apellido, edad, ciudad) 
                   VALUES (%s, %s, %s, %s)"""
        data = [
            ('Diego', 'Perez', 30, 'Quito'),
            ('María', 'Gomez', 25, 'Guayaquil'),
            ('Pedro', 'Martinez', 40, 'Cuenca'),
            ('Ana', 'Fernández', 35, 'Loja')
        ]
        cursor.executemany(query, data)
        connection.commit()
        print("Datos insertados exitosamente")
    except Error as e:
        print(f"Error al insertar datos: {e}")
    finally:
        cursor.close()

if __name__ == "__main__":
    connect()
