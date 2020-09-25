from random import choice

print('########## Desafio 19 ##########')


print('Digite 4 nomes apertando enter ao terminar cada um:\n')
name1 = input('Primeiro nome: ')
name2 = input('Segundo nome: ')
name3 = input('Terceiro nome: ')
name4 = input('Quarto nome: ')

lista = [name1, name2, name3, name4]
chosen = choice(lista)