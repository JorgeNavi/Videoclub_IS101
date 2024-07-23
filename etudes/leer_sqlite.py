import sqlite3

def rows_to_dictlist(filas, nombres):
    registros = []
    for fila in filas:
        registro = {}
        pos = 0
        for nombre in nombres:
            registro[nombre] = fila[pos]
            pos+=1
        registros.append(registro)
    return registros
    

#abrir conexión
con = sqlite3.connect("data/peliculas.sqlite")

#Crear el cursor/manejador de consultas
cur = con.cursor()

cur.execute("select id, nombre, url_foto, url_web from directores")

columns_description = cur.description
nombres_columna = []
for columna in columns_description:
    nombres_columna.append(columna[0])


#Proceso la respuesta si la hubiera
rows = cur.fetchall()

resultado = rows_to_dictlist(rows, nombres_columna)

print(resultado)


#Cerrar la conexión siempre
con.close()