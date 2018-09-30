
#ESCOLHE UM NOME ALEAÓRIO
import random


lista=list(range(3))
cont=0
for cont in range (3):

    alunos=str(input('Insira o nome dos aluno'))

    lista[cont]=alunos

escolhido=random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))