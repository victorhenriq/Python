print('########## Desafio 26 ##########')

frase2 = str(input('Digite uma frase qualquer: ')).strip().lower()
letra = str(input('Qual letra vocë quer procurar: ')).lower()

print(f'A letra "{letra}" aparece {frase2.count(f"{letra}")} vezes na frase.')
print(f'A primeira vez foi na posição {frase2.find(f"{letra}")+1} e a ultima na posição {frase2.rfind(f"{letra}")+1}')
