import numpy as np
def colocar_fpi(entrada, linha, coluna):

    line = linha
    col = coluna
    data = entrada
    aux = linha
    aux2 = coluna
    #Multiplicando por -1
    data [0] = data[0]*(-1)

    #print(values[0])
    r = data[0]
    data = np.delete(data, (0), axis=0)

    auxiliar = np.identity(linha-1, dtype=int)
    data = np.insert(data, coluna - 1, auxiliar, axis=1)
    data = np.insert(data, 0, auxiliar, axis=1)
    #print(auxiliar)

    aux3 = aux-1
    listofzeros = [0] * aux3
    l = aux2 - 1
    r = np.insert(r, l, listofzeros, axis=0 )
    r = np.insert(r, 0 , listofzeros, axis=0)

    #Concatenando data e r
    data = np.insert(data, 0, r, 0)

    return data

if (__name__ == "__main__"):
    colocar_fpi()
