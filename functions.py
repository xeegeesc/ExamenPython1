import csv

def read_data(nombreFichero):

    f = open(nombreFichero, mode="rt", encoding="utf-8")
    reader = csv.reader(file, delimiter = "\t")
    data = f.read()
    f.close()

     
