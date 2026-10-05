import sqlite3

def eliminar_empleado(id_empleado):
    conn = sqlite3.connect('Ecotech_Dbase.db')
    c = conn.cursor()
    
    c.execute("DELETE FROM Ecotech_empleados WHERE id = ?", (id_empleado,))
    conn.commit()
    
    if c.rowcount > 0:
        print(f"\n¡Empleado con ID {id_empleado} eliminado con éxito!")
    else:
        print(f"\nNo se encontró ningún empleado con el ID {id_empleado}.")
        
    conn.close()

# Código principal dentro de main.py
if __name__ == "__main__":
    print("--- GESTIÓN DE EMPLEADOS ECOTECH ---")
    id_a_borrar = input("Ingrese el ID del empleado que desea eliminar: ")
    
    if id_a_borrar.isdigit():
        eliminar_empleado(int(id_a_borrar))
    else:
        print("Por favor, ingrese un número de ID válido.")


import sqlite3
from sqlite3 import Error

conexion = sqlite3.connect('Ecotech_Dbase.db')

try:
    cursor = conexion.cursor()
    query = "SELECT * FROM Ecotech_empleados"
    cursor.execute(query)
    registro = cursor.fetchall()
    for item in registro:
        print(item)
        
except Error as ex:
    print("Error de conexion", ex)
    
finally:
    conexion.close()
    print("la conexion se ha cerrado")