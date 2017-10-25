import leitor
import fpi
import numpy as np
import ast
from io import StringIO
from numpy import matrix

def main():

    numeros = leitor.LerArquivo()

    #LINHA for int
    linha = numeros[0]
    linha = int(linha)
    linha = linha + 1
    print(" # de Linhas :  {} ".format(linha))

    #COLUNA for int
    coluna = numeros[1]
    coluna = int(coluna)
    coluna = coluna + 1
    print(" # de Colunas : {} ".format(coluna))

    #Matriz/Parser
    matriz = ast.literal_eval(numeros[2])
    matriz = np.array(matriz)

    #FPI
    print("Passando para FPI...\n")
    teste = fpi.colocar_fpi(matriz, linha, coluna)

    #Verificando se é dual ou primal

if (__name__ == "__main__"):
    main()

