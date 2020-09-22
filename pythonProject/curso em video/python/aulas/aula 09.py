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


print('########## Desafio 23 ##########')

num = int(input('Informe um número: '))
n = str(num)
print(f'Analisando o número {num}')
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')


print('########## Desafio 24 ##########')
nome = input('Digite o nome da cidade: ')
nomediv = nome.upper().split()
print("SANTO" in nomediv[0])


print('########## Desafio 25 ##########')

nome = input('Digite seu nome completo: ')
print('Vamos ver se tem Silva em seu nome')
print("SILVA" in nome.upper())

print('########## Desafio 26 ##########')

frase2 = input('Digite uma frase qualquer: ').strip().lower()
print(f'A letra "A" aparece {frase2.count("a")} vezes na frase.')
print(f'A primeira vez foi na posição {frase2.find("a")+1} e a ultima na posição {frase2.rfind("a")+1}')


name = str(input('Digite seu nome completo: ')).split()
print(f'Seu primeiro é {name[0]} e o ultimo é {name[len(name)-1]}')
