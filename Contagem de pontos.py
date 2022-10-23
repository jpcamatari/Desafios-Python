from genericpath import exists


qnt = int(input('Numero de entradas:'))

dict = {}

for i in range(qnt):
    entrada = input('Nome e ponto:')
    nome = entrada.split('-')[0]
    ponto = int(entrada.split('-')[1])

    if dict.get(nome):
        anterior = dict[nome]
        dict[nome] = ponto + anterior


    else:
        dict[nome] = ponto

print(dict)
