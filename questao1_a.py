def soma_segundos(resposta):
    #Separa os numeros em lista a partos dos espacos
    numeros = resposta.split()

    #soma os segundo inteiros

    soma = 0
    for pos in range(1, len(numeros), 2):
        soma += int(numeros[pos])

    return soma

if __name__ == '__main__':
    #recebe numeros separados por espacos
    resposta = str(input())

    print(soma_segundos(resposta))