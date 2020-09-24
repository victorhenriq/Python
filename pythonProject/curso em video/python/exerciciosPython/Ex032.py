#descobrindo se o ano é bissexto
ano = int(input('Informe um ano e eu lhe direi se é bissexto: '))
if ano % 4 == 0:
    print(f'O ano {ano} informado é bissexto.')
else:
    print(f'O ano {ano} informado não é bissexto.')
