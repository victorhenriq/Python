print('########## desafio 05 ##########')

num1 = int(input('Digite um valor: '))
ant = num1 - 1
suce = num1 + 1
print(f'O antecessor de {num1} é {ant} e o sucessor é {suce}')

print('########## desafio 06 ##########')
print('vamos ver o dobro, o triplo e a raiz quadrada desse numero')

dob = num1 * 2
trip = num1 * 3
raiz = num1 ** (1/2)

print(f'O dobro de {num1} é {dob}, o triplo é {trip} e a raiz quadrada é {raiz}')

print('########## desafio 07 ##########')

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segnda nota: '))
media = (nota1 + nota2) / 2
print(f'A média foi de {media}')

print('########## desafio 08 ##########')
metro = float(input('Digite uma medida: '))
cent = metro * 100
mm = metro * 1000

print(f'a conversão de {metro} metro(s) em centimetros é {cent} e em milimetros é {mm}')

print('########## desafio 09 ##########')
tab = int(input('Digite um valor: '))
tabu = tab * 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(tabu)

print('########## desafio 10 ##########')
money = float(input('Digite quanto de dinheiro você tem atualmente: '))
dolar = money / 3,27
print(f'Com seus {money} reais é possivel comprar {dolar} dolares')

print('########## desafio 11 ##########')
alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))
area = alt * larg
tint = area / 2

print(f'A área da parede é de {area} metros quadrados e será necessario {tint} litros de tinta para pinta-la')

print('########## desafio 12 ##########')

preco = float(input('Digite o valor do produto: '))
desc = preco / 20
newpre = preco - desc
print(f'O valor do produto com 5% de desconto é {newpre}')

print('########## desafio 13 ##########')

salary = float(input('Digite o valor do salário do funcionário: '))
increase = (salary / 100) * 15
newsalary = increase + salary

print(f'O novo salário do funcionário é: {newsalary}')
