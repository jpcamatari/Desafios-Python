from math import ceil

x = [int(input())]

#Conferindo se a quantidade de elementos na lista é impar.
for i in range(10):
    total = sum(x)
    if not len(x) % 2 == 0:
        #Diminuindo o valor do elemento central da lista, do resultado da soma de todos os valores da lista.
        total -= x[ceil((len(x)/2)-1)]
    x.append(total)

#Adicionando elementos com valor par na lista pares.
pares = []
for i in x:
    if i % 2 == 0 and i != 0:
        pares.append(i)
#Ordenando a lista e exibindo a ultima posição da lista.
pares = sorted(pares)
print(pares[-1])
