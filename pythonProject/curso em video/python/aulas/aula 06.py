print('########## Desafio 3 melhorado ##########')

num1 = int(input('Digite um valor inteiro: '))
num2 = int(input('Digite outro valor inteiro: '))
result = num1 + num2
print('O resultado da soma entre os números {} e {} é: {}'.format(num1, num2, result))
print('Obrigado pela colaboração')


print('########## Desafio 4 ##########')

val1 = input('Digite qualquer coisa: ')
print('\nVamos fazer a verificação do tipo primitivo do valor')
print(type(val1))

print('\nVerificações do que foi digitado')
print('\nO valor digitado é alfabetico?')
print(val1.isalpha())

print('\nAlfanúmerico?')
print(val1.isalnum())

print('\nDigito ?')
print(val1.isdigit())

print('\nDecimal?')
print(val1.isdecimal())
