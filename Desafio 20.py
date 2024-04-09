##Desafio 20
from random import shuffle
a1=input('\033[7;34;mPrimeiro\033[m \033[7;34;40maluno:\033[m ')
a2=input('\033[7;34;mSegundo\033[m \033[7;34;40maluno:\033[m ')
a3=input('\033[7;35;mTerceiro\033[m \033[7;35;40maluno:\033[m ')
a4=input('\033[7;35;mQuarto\033[m \033[7;35;40maluno:\033[m ')
lista=[a1,a2,a3,a4]
shuffle(lista)
print('\033[7;35;mA ordem\033[m \033[7;35;40mde apresentação\033[m '
'\033[7;35;mserá:\033[m \033[7;35;40m{}\033[m'.format(lista))