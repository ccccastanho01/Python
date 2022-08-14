from random import choice
a1= str(input('Entre com nome do primeiro aluno? '))
a2= str(input('Entre com nome do segundo aluno? '))
a3= str(input('Entre com nome do terceiro aluno? '))
a4= str(input('Entre com nome do quarto aluno? '))
lista= [a1,a2,a3,a4]
esc= choice(lista)
print('O aluno escolhido foi: {}.'.format(esc))

