import functions as f

def __main__():
    diccioRes = f.read_data('winequality.csv')
    diccWhite, diccRed = f.split(diccioRes)

    listaValoresWhite = f.reduce(diccWhite, "alcohol")
    listaValoresRed = f.reduce(diccRed, "alcohol")

    medias = f.shilouete(listaValoresWhite, listaValoresRed)

if __name__ == '__main__':
    __main__()