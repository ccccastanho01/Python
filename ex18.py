'''from math import pow,sqrt
c1=float(input('Entre com o valor do cateto 1?'))
c2= float(input('Entre com o valor do cateto 2?'))
h= sqrt(pow(c1,2)+pow(c2,2))
print(h)'''
from math import hypot
ca=float(input('Entre com o valor do cateto adjacente? '))
co=float(input('Entre com o valor do cateto oposto? '))
h= hypot(ca,co)
print('A medida da hipotenusa para o triângulo retângulo de catetos {} e {} é {:.2f}.'.format(ca,co,h))

