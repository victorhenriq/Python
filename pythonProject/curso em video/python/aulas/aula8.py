import math
from random import choice
from random import shuffle

print('########## Desafio 16 ##########')
num = float(input('Digite um número real: '))

print(math.ceil(num))

print('########## Desafio 17 ##########')

catadj = float(input('Digite o valor do cateto adjacente: '))
catopo = float(input('Digite o valor do cateto oposto: '))

hip = math.hypot(catadj, catopo)

print('O valor da hipotenusa é : {:.2f}'.format(hip))

print('########## Desafio 18 ##########')

ang = float(input('Digite o valor de um angulo: '))

cos = math.cos(ang)
sen = math.sin(ang)
tang = math.tan(ang)

print('O valor de seno é {:.2f}, do cosseno é {:.2f} e a tangente {:.2f}'.format(sen, cos, tang))


print('########## Desafio 19 ##########')


print('Digite 4 nomes apertando enter ao terminar cada um:\n')
name1 = input('Primeiro nome: ')
name2 = input('Segundo nome: ')
name3 = input('Terceiro nome: ')
name4 = input('Quarto nome: ')

lista = [name1, name2, name3, name4]
chosen = choice(lista)
print(f'O aluno(a) esclhido(a) é : {chosen}')


print('########## Desafio 20 ##########')

print('Digite o nome dos alunos que irão fazer a apresentação:\n')
name0 = input('Primeiro nome: ')
name1 = input('Segundo nome: ')
name2 = input('Terceiro nome: ')
name3 = input('Quarto nome: ')
name4 = input('Quinto nome: ')

alunos = name0, name1, name2, name3, name4

# shuffle(alunos)

print(f'A ordem de apresentação será: {shuffle(alunos)}')
