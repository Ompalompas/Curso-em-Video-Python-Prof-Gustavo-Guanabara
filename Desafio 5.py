#Desafio 005
var1=int(input('\033[0;31;40m Digite \033[m \033[1;32;41m um \033[m \033[2;31;43m número: \033[m'))
var2=var1-1
var3=var1+1
print('\033[3;30;44mAntecessor: {:.0f} \033[m \033[4;32;41m Sucessor: {:.0f} \033[m'.format(var2,var3))