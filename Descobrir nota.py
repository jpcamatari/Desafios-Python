entrada = input()
#Separando e categorizando a entrada do usuario.
nota = int(entrada.split()[0])
media = int(entrada.split()[1])

#Formula do calculo para descobrir a primeira nota do aluno e exibição na tela da nota.
nota1 = (media*2)-nota
print(nota1)
