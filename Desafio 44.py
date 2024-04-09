preço=float(input('\033[;34;mDigite o preço: '))

print('À vista em dinheiro/cheque: {}'.format(preço-(preço/100*10)))

print('À vista no cartão : {}'.format(preço-(preço/100*5)))

print('Em 2X no cartão: {}'.format(preço))

print('Em 3X ou mais {}'.format(preço+(preço/100*20)))