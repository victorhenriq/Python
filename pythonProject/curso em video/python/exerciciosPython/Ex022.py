print('########## Desafio 22 ##########')

frase = input('Digite uma frase: ').strip()

#frase com letras todas maiúsculas
framaius = frase.upper()
print(f'Frase com todas as letras maiúsculas {framaius}')

#frase com todas as letras minúsculas
framinus = frase.lower()
print(f'Assim fica a frase com todas as letras minúsculas {framinus}')

#quantas letras tem a frase desconsiderando os espaços
tamafra = len(frase) - frase.count(' ')
print(f'Essa é a quantidade de letras que tem a frase desconsiderando os espaços {tamafra}')

#quantas letras tem a primeiraa palavra
divisãofra = frase.split()
primpala = len(divisãofra[0])
print(f'Quantidade de letras que tem a primeiraa palavra {primpala}')
