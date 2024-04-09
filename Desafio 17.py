##Desafio 17
#a=float(input('Comprimento do cateto oposto: '))
#b=float(input('Comprimento do cateto adjacente: '))
#c=(a**2+b**2)**(1/2)
#print('A hipotenusa mede: {:.2f}'.format(c))

from math import hypot
a=float(input('\033[7;33;mComprimento\033[m \033[7;33;mdo cateto\033[m '
'\033[7;33;m oposto:\033[m '))
b=float(input('Comprimento do cateto adjacente: '))
c=hypot(a,b)
print('A hipotenusa mede: {:.2f}'.format(c))