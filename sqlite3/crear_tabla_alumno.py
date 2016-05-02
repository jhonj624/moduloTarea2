import sqlite3

#Conectar a la base de datos
conexion = sqlite3.connect("sqlite3/test.sqlite3")

#Seleccionar el cursor para solicitar la consulta
consulta = conexion.cursor()

sql = """
CREATE TABLE IF NOT EXISTS test(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
nombre_alumno VARCHAR(50) NOT NULL,
contrasena_alumno VARCHAR(50) NOT NULL,
fecha_subscripcion DATE NOT NULL
)"""

#Ejecutar la consulta

if (consulta.execute(sql)):
	print ("Tabla creada con exito")
else: 
	print ("Ha ocurrido un error al crear la tabla")

#Terminamos la consula
consulta.close()

#Guardamos los cambios en la base de datos
conexion.commit()

#Cerramos la conexion a la base de datos
conexion.close()

