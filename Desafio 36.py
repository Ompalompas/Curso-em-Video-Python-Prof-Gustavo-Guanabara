vlcasa=float(input('\033[1;31;mValor da casa: '))

salario=float(input('Salário do cliente: '))

anos=int(input('Quantidade de anos: '))

vlparcela=vlcasa/(anos*12)

print('Valor da prestação: {:.2f}'.format(vlparcela),end=' ')

print('O valor da parcela não pode exceder R${}'.format(salario/100*30))

if vlparcela<=salario/100*30:

    print('Parabéns! Seu financiamento foi aprovado')

else:

    print('O financiamento foi negado')
