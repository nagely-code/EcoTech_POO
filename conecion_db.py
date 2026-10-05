import sqlite3
from sqlite3 import Error
from modelos import Empleado  # Importamos la clase del modelo

class ConexionDB:
    def __init__(self, db_name='Ecotech_Dbase.db'):
        self.db_name = db_name

    def obtener_conexion(self):
        return sqlite3.connect(self.db_name)

    def listar_empleados(self):
        empleados = []
        conexion = None
        try:
            conexion = self.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, correo, Fecha_ingreso, sueldo FROM Ecotech_empleados")
            registros = cursor.fetchall()

            for fila in registros:
                # Instanciamos el objeto Empleado
                emp = Empleado(fila[0], fila[1], fila[2], "sin telefono" ,fila[3], fila[4])
                empleados.append(emp)

        except Error as ex:
            print("Error de conexión:", ex)
        finally:
            if conexion:
                conexion.close()
                print("Conexión cerrada.")

        return empleados


if __name__ == "__main__":
        
        db = ConexionDB()
        lista = db.listar_empleados()
        print("Empleados encontrados:", len(lista))