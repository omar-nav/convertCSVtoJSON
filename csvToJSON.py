import csv
import json

csvfile = open('IDM_NM.000.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("Año","Clave Ent","Entidad","Cve Municipio","Municipio","Bien jurídico afectado","Tipo de delito","Subtipo de delito","Modalidad","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
