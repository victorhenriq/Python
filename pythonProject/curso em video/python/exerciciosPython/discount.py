print('########## desafio 12 ##########')

desc = int(input('Digite  o valor do desconto: '))
preco = float(input('Digite o valor do produto: '))

#desc = preco * (desc / 100)
#newpre = preco - desc

newpre = preco - (preco * desc / 100)

print(f'O valor do produto com {desc}% de desconto é {newpre}')
