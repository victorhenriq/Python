#calculando o aumento de salario do funcionario
salario = float(input('Informe o salário do funcionário: '))
if salario > 1250:
    aumento = salario + (salario * (10 / 100))
    print(f'Para salários superiores a R$1.250,00 o aumento será de 10%: R${aumento}.')
else:
    aumento = salario + (salario * (15 / 100))
    print(f'Para salários inferiores ou iguais a R$1.250,00 o aumento será de 15%: R${aumento}.')
