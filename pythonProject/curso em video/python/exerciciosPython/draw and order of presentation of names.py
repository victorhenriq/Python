from random import shuffle

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
