#DESAFIO 12 -  NOVO VALOR DO PRODUTO

p=float(input('Entre com o valor do produto:R$ '))
pf=p*0.95
vd=p-pf
pr=p*1.08
print('O produto custa R${:.2f}\n O seu desconto foi de R${:.2f}\n E o custo final ficou em R${:.2f}'.format(p,vd,pf))
