print('='*25)
print('Formação de triângulos')
print('='*25)
s1= float(input('Entre com 1º segmento: '))
s2= float(input('Entre com 2º segmento: '))
s3= float(input('Entre com 3º segmento: '))

if s1<s2+s3 and s2<s1+s2 and s3<s1+s2:
    print('Os segmentos formam um triângulo.')
else:
    print('Os segmentos não podem formar triângulo.')