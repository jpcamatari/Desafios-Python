entrada = input()

cont = 0
silabas_separadas = list()
while cont < len(entrada):
    silabas_separadas.append(entrada[cont:cont+2])
    cont += 2

count = 0
count_silabas = list()
while count < len(silabas_separadas):
    count2 = count
    qnt_silabas = 1
    while count2 < len(silabas_separadas):
        if not count2+1 >= len(silabas_separadas):
            if silabas_separadas[count2] == silabas_separadas[count2+1]:
                qnt_silabas +=1
                posicao_atual = count2+1

            else:
                if qnt_silabas == 1:
                    posicao_atual = count2
                break
        else:
            posicao_atual = count2

        count2 += 1

    count_silabas.append((qnt_silabas, silabas_separadas[posicao_atual]))
    count = posicao_atual + 1

saida = ''
for numero, silaba in count_silabas:
    saida += f'{numero}{silaba}' if numero > 1 else (f'{silaba}')

print(saida)

