print('########## desafio 13 ##########')

salary = float(input('Digite o valor do salário do funcionário: '))
# increase = (salary / 100) * 15
# newsalary = increase + salary
newsalary = salary + (salary * 15 / 100)
print(f'O novo salário do funcionário é: {newsalary}')
