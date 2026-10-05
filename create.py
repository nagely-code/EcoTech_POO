import sqlite3

conn = sqlite3.connect('Ecotech_Dbase.db')
c = conn.cursor()

# Datos a insertar
query="INSERT INTO Ecotech_empleados (nombre, correo, Fecha_ingreso, sueldo) values('Sam Rockfor',' sam.rockfor@gmail.com','20/10/2024', 600000)"
c.execute(query)

#datos = [
    #('pedro Aguirre', 'pedro.aguirre@gmail.com', '30/02/2002', 500000),
    #('alonso Soto', 'alonso.soto@gmail.com', '30/02/2010', 900000),
    #('Maria Servia', 'maria.servia@gmail.com', '24/06/2020', 600000)
    #('Carla King', 'carla.king@gmail.com', '01/02/2026', 850000)
#]

# Insertar en la tabla Ecotech_empleados
#c.executemany('INSERT INTO Ecotech_empleados (nombre, correo, Fecha_ingreso, sueldo) VALUES (?, ?, ?, ?)', datos)

conn.commit()
conn.close()

print("¡Registros insertados con éxito!")