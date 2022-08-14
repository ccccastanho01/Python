nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nome é: {}'.format(nome))
print('Todo escrito em letras maiúsculas:{}'.format(nome.upper()))
print('Todo escrito em letras minúsculas:{}'.format(nome.lower()))
print('Quantas letras tem o seu nome: {}'.format(len(nome)-nome.count(' ')))
sep= nome.split()
print('Seu terceiro nome é: {} e é composto de: {} letras.'.format(sep[2], len(sep[2])))






