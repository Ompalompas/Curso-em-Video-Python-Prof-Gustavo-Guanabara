##Desafio 11
larg=float(input('\033[7;35;40mDigite\033[m \033[7;30;41ma '
'largura\033[m \033[7;37;40mem metros:\033[m'))
altura=float(input('Digite a altura em metros: '))
area=larg*altura
tinta=area/2
print('Para pintar uma área de {:.1f}m², você precisará de {:.1f}'
' litros de tinta.'.format(area,tinta))
##10m2 5l----100m2---50l