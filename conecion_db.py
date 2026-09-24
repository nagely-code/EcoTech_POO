import sqlite3

class conexion:
    def conexionBaseDeDatos():
        try:
            conexion = sqlite3.connect('Ecotech_Dbase.db')
            print("conexion exitosa")
            return conexion
        except sqlite3.Error as ex :
            print("Error de conexion", ex)
            
conexion.conexionBaseDeDatos()