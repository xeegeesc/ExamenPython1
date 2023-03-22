import csv

def read_data(nombreFichero):
    diccionario = {}
    indices = ["type","fixed" "acidity","volatile" "acidity","citric acid","residual sugar","chlorides","free sulfur dioxide","total sulfur dioxide","density","pH","sulphates","alcohol","quality"]
    with open(nombreFichero, 'r') as file:
        reader = csv.reader(file)
        j=0
        for row in reader:
            i=0
            for dato in row:
                diccionario["dato"+j]={indices[i]+":"+dato}
                i+=1
            j+=1

    print(diccionario)
def __main__():
    read_data('winequality.csv')

if __name__ == '__main__':
    __main__()