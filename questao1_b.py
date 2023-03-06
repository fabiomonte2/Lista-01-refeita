def soma_terceiros(resposta:str):
    #Separa os numeros em lista a partos dos espacos
    numeros = resposta.split()

    #soma os terceiros inteiros

    soma = 0
    for pos in range(2, len(numeros), 3):
        soma += int(numeros[pos])

    return soma
    
if __name__ == '__main__':
    #recebe numeros separados por espacos
    resposta = str(input())

    print(soma_terceiros(resposta))