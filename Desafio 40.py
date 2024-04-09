nota1=float(input('\033[1;36;mPrimeira nota: '))

nota2=float(input('Segunda nota: '))

media=(nota1+nota2)/2

if media<5:

    print('Você foi reprovado. Se esforce mais na próxima vez')

if media>=5:

    if media<7:

        print('Você ficou em recuperação. Bons estudos!')

    else:

        print('Você foi aprovado. Bom trabalho!')