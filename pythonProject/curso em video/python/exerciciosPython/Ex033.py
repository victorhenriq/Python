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
