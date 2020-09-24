from random import randrange


#descobrir um numero sorteado pela maquina
comp = randrange(0, 5)
num = int(input('Qual valr de 0 a 5 que você que o computador escolheu?: '))
if num == comp:
    print('Parabéns você acertou !!!')
else:
    print('Não foi dessa vez HEHEHEE')
print(f'O número sorteado foi {comp}')


#calculando uma multa
velocidade = float(input('Informe a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'A velocidade de {velocidade}km está acima do limite de 80km. O valor da multa será de: R${multa}')

#descobrindo se é par ou impar
n = int(input('Informe um número e lhe direi se é par ou impar: '))
if n % 2 == 0:
    print(f'O número {n} é PAR.')
else:
    print(f'O número {n} é ÍMPAR.')


#calculando o preço da viagem
distancia = float(input('Informe a distância da viagem em km: '))
if distancia <= 200:
    valor = distancia * 0.50
    print (f'Viagens de até 200km custam R$0,50 por km. Portanto o valor da sua viagem será de R${valor}.')
else:
    valor = distancia * 0.45
    print (f'Viagens acima de 200km custam R$0,45 por km. Portanto o valor da sua viagem será de R${valor}.')

#descobrindo se o ano é bissexto
ano = int(input('Informe um ano e eu lhe direi se é bissexto: '))
if ano % 4 == 0:
    print(f'O ano {ano} informado é bissexto.')
else:
    print(f'O ano {ano} informado não é bissexto.')


#descobrindo qual número é o maior
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'O número {n1} é o maior !!')
if n2 > n1 and n2 > n3:
    print(f'O número {n2} é o maior deles !!')
if n3 > n1 and n3 > n2:
    print(f'Onumero {n3} é o maior de todos')


#calculando o aumento de salario do funcionario
salario = float(input('Informe o salário do funcionário: '))
if salario > 1250:
    aumento = salario + (salario * (10 / 100))
    print(f'Para salários superiores a R$1.250,00 o aumento será de 10%: R${aumento}.')
else:
    aumento = salario + (salario * (15 / 100))
    print(f'Para salários inferiores ou iguais a R$1.250,00 o aumento será de 15%: R${aumento}.')

