import sqlite3

conn = sqlite3.connect('Ecotech_Dbase.db')
c = conn.cursor()

# Datos a insertar
datos = [
    ('pedro Aguirre', 'pedro.aguirre@gmail.com', '30/02/2002', 500000),
    ('alonso Soto', 'alonso.soto@gmail.com', '30/02/2010', 900000)
]

# Insertar en la tabla Ecotech_empleados
c.executemany('INSERT INTO Ecotech_empleados (nombre, correo, Fecha_ingreso, sueldo) VALUES (?, ?, ?, ?)', datos)

conn.commit()
conn.close()

print("¡Registros insertados con éxito!")