m=float(input('Insira a medida em metros:'))
mm=m*1000
cm=m*100
dm=m*10
dam=m/10
hm=m/100
km=m/1000
print('A medida em milímetros vale: {:.0f}\nEm centímetros vale: {:.0f}\nEm decímetros vale: {:.1f}  '.format(mm,cm,dm))
print('A medida em decâmetros vale: {}\nEm hectometros vale: {}\nEm quilômetros vale: {}  '.format(dam,hm,km))
