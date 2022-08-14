km=int(input('Quantos quilômetros o carro rodou? '))
d=int(input('Quantos dias ele ficou alugado? '))
c=(60 * d) + (0.15 * km)
print('O veículo rodou {}Km, ficou alugado {} dias e gerou um custo total de {} reis.'.format(km, d, c))


