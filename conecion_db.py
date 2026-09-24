import sqlite3

def conn_db():
    try:
        conexion = sqlite3.connect("ecotech_sti.db")
        cursor = conexion.cursor()

        cursor.execute()

    