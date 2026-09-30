import sqlite3

def eliminar_empleado(id):
    conexion = None
    
    try:
        conexion = sqlite3.connect('Ecotech_Dbase.db')
        cursor = conexion.cursor()
        
        consulta_sql = "DELETE FROM Ecotech_empleados WHERE id = ?"
        cursor.execute(consulta_sql, (id))
        
        conexion.commit()
        
        
        if cursor.rowcount > 0:
            print(f" El empleado con el ID {id} fue despedido correctamente")
            
        else:
            print(f" No se encontro ningun empleado con el id {id}.")
            
    except sqlite3.Error as ex:
        print(f" Error al conectar a la base de datos o despedir.")
            
    finally:
        if conexion:
            conexion.close()
            print("conexion cerrada")
            
            