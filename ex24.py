n= int(input('Entre com um número inteiro entre 0 e 9999? '))
u= n // 1 % 10
d= n// 10 % 10
c= n// 100 % 10
m= n// 1000% 10
print('O número escolhido foi: {}\n Unidades: {}\n Dezenas: {}\n Centenas: {}\n Milhares: {}'.format(n, u, d, c, m))


