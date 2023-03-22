import csv
import math

def read_data(nombreFichero):
    diccionario = {}
    diccionarioAux = {}
    indices = ["type","fixed" "acidity","volatile" "acidity","citric acid","residual sugar","chlorides","free sulfur dioxide","total sulfur dioxide","density","pH","sulphates","alcohol","quality"]
    with open(nombreFichero, 'r') as file:
        reader = csv.reader(file)
        j=0
        for row in reader:
            i=0
            for dato in row:
                diccionarioAux[indices[i]] =dato
                i+=1

            if(j==0):
                diccionarioAux={}

        
            diccionario["dato"+str(j)]= diccionarioAux
            diccionarioAux = {}
            j+=1
        coincidencia = []
        for dato in diccionario:
            for dato2 in diccionario[dato]:
                valor = diccionario[dato][dato2]
                if(valor == ""):
                    if(dato not in coincidencia):
                        coincidencia.append(dato)
        
        for dato in coincidencia:
            del diccionario[dato]
        
        del diccionario["dato0"]

        if(len(diccionario)<10):
            raise ValueError("Ha ocurrido la excepción: 'El diccionario tiene menos de 10 elementos' en la función 'read_data'")
        else:
            #print(diccionario)
            return diccionario
        
        
def split(diccionario):
    diccionarioRed = {}
    diccionarioWhite = {}

    for dato in diccionario:
        if (diccionario[dato]["type"] == "white"):
            del diccionario[dato]["type"]
            diccionarioWhite[dato]=diccionario[dato]
        else:
            del diccionario[dato]["type"]
            diccionarioRed[dato]=diccionario[dato]
    
    return (diccionarioWhite, diccionarioRed)

def reduce(diccionario, atributo):
    listaValores = []

    for dato in diccionario:
        if(atributo not in diccionario[dato]):
            raise ValueError("Ha ocurrido la excepción: 'El atributo no existe en el dato' en la función 'reduce'")

        else:
            listaValores.append(diccionario[dato][atributo])

    return listaValores

def shilouete(lista1, lista2):

    i = 0
    ai = 0
    aiAux = []
    for valor in lista1:

        aiAux.append( math.sqrt(math.pow(abs(valor-lista1[i+1]))))

        i+=1

