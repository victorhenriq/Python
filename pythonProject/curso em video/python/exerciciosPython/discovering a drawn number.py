from random import randrange


#descobrir um numero sorteado pela maquina
comp = randrange(0, 5)
num = int(input('Qual valr de 0 a 5 que você que o computador escolheu?: '))
if num == comp:
    print('Parabéns você acertou !!!')
else:
    print('Não foi dessa vez HEHEHEE')
print(f'O número sorteado foi {comp}')