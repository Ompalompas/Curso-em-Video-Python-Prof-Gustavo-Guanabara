#Desafio 12
preço=float(input('\033[7;30;42mDigite\033[m \033[7;30;43mo preço\033[m '
'\033[7;30;44mdo produto:\033[m'))
desconto=preço/100*5
total=preço-desconto
print('Valor a pagar R${:.2f} Você recebeu um desconto de 5% = R${:.2f}'.format(total,desconto))
