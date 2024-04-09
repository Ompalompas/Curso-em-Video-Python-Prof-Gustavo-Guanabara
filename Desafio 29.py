vel=float(input('\033[2;32;41mDigite\033[m \033[2;30;42ma velocidade\033[m '
                '\033[2;30;43mdo carro:\033[m '))
km=vel-80

if vel>80:

    print('\033[2;30;44mVocê\033[m \033[2;30;45mfoi\033[m \033[2;30;46mmultado\033[m '
          '\033[2;30;47mno\033[2;33;m \033[2;33;40mvalor\033[m \033[2;33;41mde\033[m'
          ' \033[2;33;mR${:.2f}\033[m'.format(km*7))
