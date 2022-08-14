sal = float(input('Qual o atual salário do funcionário? R$'))
if sal <= 1250:
    print('O aumento será de {:.2f} reais e o salário passará para {:.2f} reais.'.format(sal*0.15, sal*1.15))
else:
    print('O aumento será de {:.2f} reais e o salário passará para {:.2f} reais.'.format(sal*0.10, sal*1.10))