distancia = int(input('Entre com a distância percorrida: '))
if distancia <= 200:
    print('O custo do total da viagem foi de R${:.2f}'.format(distancia*0.50))
else:
    print('O custo total da viagem foi de R${:.2f}'.format(distancia*0.45))
