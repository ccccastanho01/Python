from random import randint
from time import sleep
computador = randint(0,5) #NºESCOLHIDO PELO COMPUTADOR
usuario= int(input('Entre com um número de 0 a 5? '))
sleep(2)
if usuario == computador:
    print('Eu escolhi o número {} também.Parabéns você acertou!!'.format(computador))
else:
    print('Tente novamente!!!')
