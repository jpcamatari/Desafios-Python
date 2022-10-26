<h1>Exercício Língua do MAFAGAFO</h1>
<h3>Descrição:</h3>
<p>
Pedrinho e seus amigos criaram uma nova forma de se comunicar, eles apelidaram de
língua do MAFAGAFO.<br>
Funciona da seguinte forma, todas as palavras são formadas por: MA, FA, GA, FO
Uma simples palavra escrita por pedrinho na língua do MAFAGAFO ficou assim:
FAFAGAFAFOFOFOMAMAMA<br>
Após alguns minutos observando, Pedrinho percebeu que existe uma forma mais eficiente
de escrever essa palavra comprimindo os dados.<br>
A palavra FAFAGAFAFOFOFOMAMAMA ficaria comprida da seguinte forma:
2FAGAFA2FO3MA<br>
Ou seja, sempre que MA, FA, GA ou FO, se repetir 2 ou mais vezes será incluído o número
de repetições antes da sílaba e caso a sílaba apareça uma única vez ela permanece da
mesma forma.<br>
Exemplos:<br>
______________________________________________________________<br>
Entrada Saída<br>
MAFAFAGAGAGAGAFOFOFO MA2FA4GA3FO<br>
______________________________________________________________<br>
Entrada Saída<br>
GAGAGAGAFAFAFOMAMAMAMAMA 4GA2FAFO5MA<br>
______________________________________________________________<br>
Entrada Saída<br>
MAFAGAFO MAFAGAFO<br>
</p>

<h1>Exercício Contagem de Pontos</h1>
<h3>Descrição:</h3>
<p>
Um grupo de amigos costumam realizar algumas apostas todos os dias e anotam o nome e
a quantidade de pontos do vencedor, ao final do mês eles precisam ordenar todos os
amigos para saberem quais foram os melhores colocados, mas como isso é um muito
trabalhoso o grupo pediu para os alunos da Python Full ajudar a realizar esse cálculo.
A anotação dos amigos seguem a seguinte regra: o nome da pessoa, uma barra e depois a
quantidade de pontos, tudo sem espaço.<br>
Por final, a sua aplicação deve retornar o nome dos amigos de forma ordenada em relação
aos pontos<br>
Entrada:<br>
a primeira linha corresponde a quantidade de dados anotados e as linhas posteriores ao
nome e a quantidade de pontos de cada um<br>
Exemplos:<br>
______________________________________________________________<br>
Entrada Saída<br>
6 PEDRO<br>
JOAO-10 JOAO<br>
PEDRO-20 MARCOS<br>
MARCOS-3<br>
PEDRO-1<br>
JOAO-5<br>
MARCOS-5<br>
______________________________________________________________<br>
Entrada Saída<br>
4 CAIO<br>
ROGERIO-2 ROGERIO<br>
CAIO-1<br>
CAIO-1<br>
CAIO-1<br>
</p>
<h1>Exercício Descobrir Notas</h1>
<h3>Descrição</h3>
<p>
Caio é um aluno da Pythonando onde as notas funcionam da seguinte forma: o aluno
realiza duas provas e por fim é calculado a média entre essas duas notas.<br>
Lembrando que a fórmula para o cálculo da média é: media = (nota1 + nota2)/2
Como a prova 1 foi realizada a muito tempo atrás, Caio acabou esquecendo a sua nota e
lembra apenas de sua média e a nota da segunda prova, com essas informações ele pediu
para você criar uma aplicação que recebe a nota da prova 2 e a média e informa qual foi
sua nota na primeira prova.<br>
Entradas<br>
Uma única linha contendo a nota da prova dois e a média separadas por espaço<br>
Entrada Saída<br>
5 7 9<br>
______________________________________________________________<br>
Entrada Saída<br>
10 6 2<br>
______________________________________________________________<br>
</p>
<h1>Exercício Lista</h1>
<h3>Descrição:</h3>
<p>
Receba um valor x e crie uma lista de 11 posições sabendo que a próxima
posição é a soma de todos os valores anteriores e caso a quantidade de
elementos da lista seja ímpar deve desconsiderar o valor central para realizar
a soma.<br>
Dado X como 3, a lista seria populada da seguinte forma:<br>
[3]<br>
[3, 0]<br>
[3, 0, 3]<br>
[3, 0, 3, 6]<br>
[3, 0, 3, 6, 12]<br>
[3, 0, 3, 6, 12, 21]<br>
[3, 0, 3, 6, 12, 21, 45]<br>
[3, 0, 3, 6, 12, 21, 45, 84]<br>
[3, 0, 3, 6, 12, 21, 45, 84, 174]<br>
[3, 0, 3, 6, 12, 21, 45, 84, 174, 336]<br>
[3, 0, 3, 6, 12, 21, 45, 84, 174, 336, 684]<br>
Por fim, exiba o maior número par encontrado dentro da lista gerada, caso
não exista nenhum número par exibir: "Não encontrado!”.<br>
Entrada Saída<br>
3 684<br>
______________________________________________________________<br>
Entrada Saída<br>
13 2964<br>
______________________________________________________________<br>
Entrada Saída<br>
5 1140<br>
__________________________________________________________<br>
</p>