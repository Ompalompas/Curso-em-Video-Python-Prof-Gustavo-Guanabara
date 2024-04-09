maior=0
saida=0

while saida != 1:
    valor1 = int(input('Digite um valor: '))
    valor = int(input('Digite outro valor: '))

    print(' [1] SOMAR \n [2] MULTIPLICAR \n [3] MAIOR \n [4] REINICIAR \n [5] SAIR DO PROGRAMA ' )
    opcao=int(input(''))

    if opcao==1:
        print('A soma entre {} e {} dá {}'.format(valor,valor1,valor+valor1))

    if opcao==2:
        print('A multiplicação entre {} e {} dá {}'.format(valor1, valor, valor1*valor))

    if opcao==3:
        if valor1>valor:
            maior+=valor1
        else:
            maior+=valor
        print('O valor maior é {}'.format(maior))

    if opcao==5:
        saida+=1





