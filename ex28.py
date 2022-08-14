n= str(input('Qual seu nome completo? ')).strip()
nome = n.split()
print('Seu nome é: {}.'.format(nome[0]))
print('Seu último sobrenome é: {}.'.format(nome[len(nome)-1]))




