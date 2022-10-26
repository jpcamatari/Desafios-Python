#Input do usuario para definir a quantidade de vezes q o loop for vai rodar.
qnt = int(input('Numero de entradas:'))

dict = {}
#Entrada de dados do usuario com informações de nome e pontos a serem adicionadas a contagem.
for i in range(qnt):
    entrada = input('Nome e ponto:')
    nome = entrada.split('-')[0]
    ponto = int(entrada.split('-')[1])
#Confere se ja existe o nome na lista, e se existir adiciona o ponto a pessoa, e se não existir, adiciona nome e ponto.
    if dict.get(nome):
        anterior = dict[nome]
        dict[nome] = ponto + anterior


    else:
        dict[nome] = ponto

#Ordena pelo maior pontuador, e retorna na tela o nome.
for i in sorted(dict, key= dict.get, reverse=True):
    print(i)