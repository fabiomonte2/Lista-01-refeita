from questao1_a import soma_segundos
from questao1_b import soma_terceiros

resposta = str(input())

terceiro_soma = soma_terceiros(resposta)
segundo_soma = soma_segundos(resposta)

if terceiro_soma > segundo_soma:
    print(True)
else:
    print(False)

