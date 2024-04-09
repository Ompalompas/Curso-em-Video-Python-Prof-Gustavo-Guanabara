n=input('\033[1;30;46mDigite\033[m \033[1;30;47mseu\033[m '
        '\033[1;38;mnome\033[m \033[1;;40mcompleto:\033[m ').strip()

nome=n.split()

print('\033[1;38;41mMuito\033[m \033[1;30;42mprazer\033[m '
      '\033[1;30;43mem\033[m \033[1;30;44mte\033[m '
      '\033[1;30;45mconhecer!\033[m')

print('\033[1;30;46mSeu\033[m \033[1;30;47mprimeiro\033[m '
      '\033[1;30;mnome\033[m \033[1;30;40mé\033[m '
      '\033[1;30;41m{}\033[m'.format(nome[0]))

print('\033[1;30;42mSeu\033[m \033[2;;40mútimo\033[m '
      '\033[2;30;41mnome\033[m \033[2;30;mé\033[m '
      '\033[2;30;43m{}\033[m.'.format(nome[len(nome)-1]))