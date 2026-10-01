import sqlite3

from sqlite3 import Error
conexion=sqlite3.connect('Ecotech_Dbase.db')

try:
    cursor = conexion.cursor()
    query = "SELECT * FROM Ecotech_empleados "
    cursor.execute(query)
    registro=cursor.fetchall()
    for item in registro:
        print(item)
        
except Error as ex:
    print("Error de conexion", ex)
    
finally:
    conexion.close()
    print(" La conexion se ha cerrado")
    