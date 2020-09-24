#calculando uma multa
velocidade = float(input('Informe a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'A velocidade de {velocidade}km está acima do limite de 80km. O valor da multa será de: R${multa}')

