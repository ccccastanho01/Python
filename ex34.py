n1 = int(input('Entre com 1º valor: '))
n2 = int(input('Entre com 2º valor: '))
n3 = int(input('Entre com 3º valor: '))

menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('O menor nº é {}'.format(menor))

maior = n2
if n1>n2 and n1>n3:
    maior = n1
if n3>n1 and n3>n2:
    maior = n3
print('O maior nº é {}'.format(maior))