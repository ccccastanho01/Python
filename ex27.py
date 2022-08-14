frase = str(input('Entre com uma frase: ')).strip().upper()
print('Quantas vezes a letra A aparece na frase? {} vezes.'.format(frase.count('A')))
print('Em qual posição aparece a primeira letra A? {}ª posição.'.format(frase.find('A')+1))
print('Em qual posição aparece a última letra A? {}ª posição.'.format(frase.rfind('A')+1))



