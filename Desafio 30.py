n1=int(input('\033[1;33;mDigite um número:\033[m '))

n2=int(n1%2)

if n2==0:

    print('\033[1;33;mO número que você\033[m'
          ' \033[1;33;mdigitou {} é PAR\033[m'.format(n1))
else:
    print('\033[1;33;mO número\033[m \033[1;33;mque\033[m \033[1;33;mvocê\033[m'
          ' \033[1;33;mdigitou {} é ÍMPAR\033[m'.format(n1))