salario=float(input('\033[1;32;mValor do salário:\033[m '))

if salario>1249:

    aumento=salario/100*10

    print('\033[1;32;mParabéns você recebeu um aumento de 10%!')

    print('Salário atual: R$\033[m{:.2f}'.format(salario+aumento))

else:

    aumento=salario/100*15

    print('\033[1;32;mVocê recebeu um aumento de 15%')

    print('Salário atual: R$\033[m{:.2f}'.format(salario+aumento))