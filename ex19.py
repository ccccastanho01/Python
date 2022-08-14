import math
angulo=float(input('Digite um ângulo qualquer?'))
seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))
print("Qual foi o ângulo escolhido {}º\n Qual o valor do seu seno? {:.2f}\n Qual o valor do seu cosseno? {:.2f}\n Qual o valor da sua tangente?{:.2f}"
.format(angulo,seno,cosseno,tangente))



