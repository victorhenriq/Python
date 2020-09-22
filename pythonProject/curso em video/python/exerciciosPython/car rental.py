print('########## Desafio 15 ##########')

dia = int(input('Digite a quantidade de dias que o carro foi usado: '))
km = float(input('Digite a quantidade de km rodados: '))
priceday = dia * 60
pricekm = km * 0.15

totalprice = priceday + pricekm

print(f'O valor diario é de R${priceday} e dos kilometros foi de R${pricekm},', end='')
print(f' o valor total do aluguel do carro foi de R${totalprice}')