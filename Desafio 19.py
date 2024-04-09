##Desafio 19
from random import choice
aluno1=input('\033[7;33;mPrimeiro\033[m \033[7;33;maluno:\033[m ')
aluno2=input('\033[7;33;mSegundo\033[m \033[7;33;maluno:\033[m ')
aluno3=input('\033[7;33;mTerceiro\033[m \033[7;33;maluno:\033[m ')
aluno4=input('\033[7;33;mQuarto\033[m \033[7;34;maluno:\033[m ')
lista=[aluno1,aluno2,aluno3,aluno4]
escolhido=choice(lista)
print('\033[7;34;40mO aluno\033[m \033[7;34;mescolhido\033[m \033[7;34;mfoi\033[m'
' \033[7;34;m{}\033[m'.format(escolhido))
