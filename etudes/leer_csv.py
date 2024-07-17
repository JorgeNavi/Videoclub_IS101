import csv

fichero = open("data\directores.csv", "r", newline="")

lector_csv = csv.reader(fichero, delimiter=";", quotechar="'")

for registro in lector_csv:
    print(registro)

fichero.close()

print("-----------------------------------------------------")

#ahora como diccionario

fichero = open("data\directores.csv", "r", newline="")

lector_csv_diccionario = csv.DictReader(fichero, delimiter=";", quotechar="'")

for registro in lector_csv_diccionario:
    print(registro)

fichero.close()