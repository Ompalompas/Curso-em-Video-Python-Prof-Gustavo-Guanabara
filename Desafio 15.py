##Desafio 15
diasalugados=int(input('\033[7;31;46mDigite\033[m \033[7;31;47ma quantidade\033[m '
'\033[7;32;40mde dias\033[m \033[7;32;41m alugados:\033[m'))
kmpercorridos=float(input('Digite a quantidade de km percorridos: '))
calc=(kmpercorridos*0.15)+(diasalugados*60)
print('{:.0f}km percorridos durante o período de {} dias, valor a cobrar R${:.2f}'.format(kmpercorridos,diasalugados,calc))