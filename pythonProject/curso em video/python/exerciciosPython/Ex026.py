print('########## Desafio 26 ##########')

frase2 = input('Digite uma frase qualquer: ').strip().lower()
print(f'A letra "A" aparece {frase2.count("a")} vezes na frase.')
print(f'A primeira vez foi na posição {frase2.find("a")+1} e a ultima na posição {frase2.rfind("a")+1}')
