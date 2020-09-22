from math import hypot

print('########## Desafio 17 ##########')

catadj = float(input('Digite o valor do cateto adjacente: '))
catopo = float(input('Digite o valor do cateto oposto: '))

hip = hypot(catadj, catopo)

print('O valor da hipotenusa é : {:.2f}'.format(hip))
