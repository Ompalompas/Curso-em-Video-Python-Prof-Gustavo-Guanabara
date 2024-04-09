'''import math
from math import factorial

n=int(input('Digite um número: '))
r=factorial(n)

print('O fatorial de {} é {}'.format(n,r))

############# UTILIZANDO LAÇO WHILE ################

r = int(input('Digite um número para calcular seu fatorial: '))
c=r
f=1

print('Calculando fatorial de {}! = '.format(r), end='')

while c >0:

    print('{} '.format(c), end='')
    print(' x ' if c >1 else ' = ', end='')
    f *=c
    c -= 1

print('{}'.format(f))'''

######### UTILIZANDO LAÇO FOR ####################
r = int(input('Digite um número para calcular seu fatorial: '))
c=r
f=1

print('Calculando fatorial de {}! = '.format(r), end='')

for c in range(r,0,-1):

    print('{} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print('{}'.format(f))









