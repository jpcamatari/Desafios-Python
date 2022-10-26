<h1>Exercício Língua do MAFAGAFO</h1>
<h3>Descrição:</h3>
<p>
Pedrinho e seus amigos criaram uma nova forma de se comunicar, eles apelidaram de
língua do MAFAGAFO.
Funciona da seguinte forma, todas as palavras são formadas por: MA, FA, GA, FO
Uma simples palavra escrita por pedrinho na língua do MAFAGAFO ficou assim:
FAFAGAFAFOFOFOMAMAMA
Após alguns minutos observando, Pedrinho percebeu que existe uma forma mais eficiente
de escrever essa palavra comprimindo os dados.
A palavra FAFAGAFAFOFOFOMAMAMA ficaria comprida da seguinte forma:
2FAGAFA2FO3MA
Ou seja, sempre que MA, FA, GA ou FO, se repetir 2 ou mais vezes será incluído o número
de repetições antes da sílaba e caso a sílaba apareça uma única vez ela permanece da
mesma forma.
Exemplos:
______________________________________________________________
Entrada Saída
MAFAFAGAGAGAGAFOFOFO MA2FA4GA3FO
______________________________________________________________
Entrada Saída
GAGAGAGAFAFAFOMAMAMAMAMA 4GA2FAFO5MA
______________________________________________________________
Entrada Saída
MAFAGAFO MAFAGAFO
</p>

<h1>Exercício Contagem de Pontos</h1>
<h3>Descrição:</h3>
<p>
Um grupo de amigos costumam realizar algumas apostas todos os dias e anotam o nome e
a quantidade de pontos do vencedor, ao final do mês eles precisam ordenar todos os
amigos para saberem quais foram os melhores colocados, mas como isso é um muito
trabalhoso o grupo pediu para os alunos da Python Full ajudar a realizar esse cálculo.
A anotação dos amigos seguem a seguinte regra: o nome da pessoa, uma barra e depois a
quantidade de pontos, tudo sem espaço.
Por final, a sua aplicação deve retornar o nome dos amigos de forma ordenada em relação
aos pontos
Entrada:
a primeira linha corresponde a quantidade de dados anotados e as linhas posteriores ao
nome e a quantidade de pontos de cada um
Exemplos:
______________________________________________________________
Entrada Saída
6 PEDRO
JOAO-10 JOAO
PEDRO-20 MARCOS
MARCOS-3
PEDRO-1
JOAO-5
MARCOS-5
______________________________________________________________
Entrada Saída
4 CAIO
ROGERIO-2 ROGERIO
CAIO-1
CAIO-1
CAIO-1
</p>
<h1>Exercício Descobrir Notas</h1>
<h3>Descrição</h3>
<p>
Caio é um aluno da Pythonando onde as notas funcionam da seguinte forma: o aluno
realiza duas provas e por fim é calculado a média entre essas duas notas.
Lembrando que a fórmula para o cálculo da média é: media = (nota1 + nota2)/2
Como a prova 1 foi realizada a muito tempo atrás, Caio acabou esquecendo a sua nota e
lembra apenas de sua média e a nota da segunda prova, com essas informações ele pediu
para você criar uma aplicação que recebe a nota da prova 2 e a média e informa qual foi
sua nota na primeira prova.
Entradas
Uma única linha contendo a nota da prova dois e a média separadas por espaço
Entrada Saída
5 7 9
______________________________________________________________
Entrada Saída
10 6 2
______________________________________________________________
</p>
<h1>Exercício Lista</h1>
<h3>Descrição:</h3>
<p>
Receba um valor x e crie uma lista de 11 posições sabendo que a próxima
posição é a soma de todos os valores anteriores e caso a quantidade de
elementos da lista seja ímpar deve desconsiderar o valor central para realizar
a soma.
Dado X como 3, a lista seria populada da seguinte forma:
[3]
[3, 0]
[3, 0, 3]
[3, 0, 3, 6]
[3, 0, 3, 6, 12]
[3, 0, 3, 6, 12, 21]
[3, 0, 3, 6, 12, 21, 45]
[3, 0, 3, 6, 12, 21, 45, 84]
[3, 0, 3, 6, 12, 21, 45, 84, 174]
[3, 0, 3, 6, 12, 21, 45, 84, 174, 336]
[3, 0, 3, 6, 12, 21, 45, 84, 174, 336, 684]
Por fim, exiba o maior número par encontrado dentro da lista gerada, caso
não exista nenhum número par exibir: "Não encontrado!”.
Entrada Saída
3 684
______________________________________________________________
Entrada Saída
13 2964
______________________________________________________________
Entrada Saída
5 1140
__________________________________________________________
</p>