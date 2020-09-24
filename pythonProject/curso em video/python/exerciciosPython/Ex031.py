#calculando o preço da viagem
distancia = float(input('Informe a distância da viagem em km: '))
if distancia <= 200:
    valor = distancia * 0.50
    print (f'Viagens de até 200km custam R$0,50 por km. Portanto o valor da sua viagem será de R${valor}.')
else:
    valor = distancia * 0.45
    print (f'Viagens acima de 200km custam R$0,45 por km. Portanto o valor da sua viagem será de R${valor}.')
