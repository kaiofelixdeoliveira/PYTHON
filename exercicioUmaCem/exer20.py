
import random

lista=list(range(4))
cont=0
for cont in range (4):

    alunos=str(input('Insira o nome dos aluno'))

    lista[cont]=alunos


random.shuffle(lista)
print('O aluno escolhido foi {}'.format(lista))