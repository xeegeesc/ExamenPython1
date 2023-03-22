import csv

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
        listaValores.append(diccionario[dato][atributo])
    return listaValores

def __main__():
    diccioRes = read_data('winequality.csv')
    diccWhite, diccRed = split(diccioRes)

    listaValoresWhite = reduce(diccWhite, "alcohol")
    listaValoresRed = reduce(diccRed, "alcohol")

    

if __name__ == '__main__':
    __main__()