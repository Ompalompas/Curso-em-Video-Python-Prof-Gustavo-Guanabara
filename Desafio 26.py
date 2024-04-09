frase=input('\033[1;30;47mDigite\033[m \033[1;35;muma\033[m '
'\033[1;35;40mfrase:\033[m ').lower().strip()

print('\033[1;35;41mA\033[m \033[1;30;42mletra\033[m '
'\033[1;30;43m(a)\033[m \033[1;30;44maparece\033[m '
'\033[1;30;45m{}\033[m \033[1;30;46mvezes\033[m '
'\033[1;30;47mna\033[m \033[1;36;mfrase.\033[m'.format(frase.count('a')))

print('\033[1;36;40mA\033[m \033[1;36;41mprimeira\033[m '
'\033[1;30;42mletra\033[m \033[1;30;43m(a)\033[m '
'\033[1;30;44mapareceu\033[m \033[1;30;45mna\033[m '
'\033[1;30;46m{}\033[m \033[1;30;47mposição\033[m'.format(frase.find('a')+1))
tamfrase=len(frase)

print('\033[1;37;mA\033[m \033[1;37;40múltima\033[m \033[1;37;41mletra\033[m '
'\033[1;30;42mapareceu\033[m \033[1;30;43mna\033[m \033[1;30;44mposição\033[m '
'\033[1;30;45m{}\033[m'.format(tamfrase))

#print('A última letra A apareceu na posição {}'.format(frase.rfind('a')+1))