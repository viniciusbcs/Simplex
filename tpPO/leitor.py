def LerArquivo():

    arquivo = open("entrada.txt", "r")
    conteudo = []

    for linha in arquivo:
        linha = linha.strip()
        conteudo.append(linha)

    arquivo.close()
    #print(type(conteudo))
    return conteudo

if (__name__ == "__main__"):
    LerArquivo()
