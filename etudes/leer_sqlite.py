import sqlite3

#abrir conexión
con = sqlite3.connect("data/peliculas.sqlite")

#Crear el cursor/manejador de consultas
cur = con.cursor()

cur.execute("select id, nombre, url_foto, url_web from directores")

#Proceso la respuesta si la hubiera
result = cur.fetchall()

print(result)

#Cerrar la conexión siempre
con.close()