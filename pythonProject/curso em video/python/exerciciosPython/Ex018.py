from math import cos
from math import tan
from math import sin

print('########## Desafio 18 ##########')

ang = float(input('Digite o valor de um angulo: '))

cos = cos(ang)
sen = sin(ang)
tang = tan(ang)

print('O valor de seno é {:.2f}, do cosseno é {:.2f} e a tangente {:.2f}'.format(sen, cos, tang))
