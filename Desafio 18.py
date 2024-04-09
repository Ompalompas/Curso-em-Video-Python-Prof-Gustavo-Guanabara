##Desafio 18
import math
angulo=float(input('\033[7;33;mDigite\033[m \033[7;33;40mum ângulo:\033[m'))
seno=math.sin(math.radians(angulo))
cos=math.cos(math.radians(angulo))
tang=math.tan(math.radians(angulo))
print('O seno é: {:.2f}'.format(seno))
print('O cosseno é: {:.2f} e a tangente é: {:.2f}'.format(cos,tang))
