from random import choice

n1=[0,1,2,3,4,5]

n2=int(choice(n1))

n3=int(input('\033[2;30;44mTente\033[m \033[2;30;45madivinhar\033[m'
    ' \033[2;30;46mum\033[m \033[2;30;47mnúmero\033[m \033[2;;mde\033[m '
    '\033[2;31;m0 à 5:\033[m '))

if n3==n2:
    print('\033[2;31;40mVocê\033[m \033[2;;41mganhou,\033[m '
          '\033[2;31;42mparabéns!\033[m')

else:
    print('\033[2;31;43mVocê\033[m \033[2;31;44mperdeu,\033[m \033[2;31;44mtente'
          '\033[2;31;45m novamente!\033[m')

print('\033[2;31;46mO número\033[m \033[2;31;47msorteado\033[m \033[2;32;mfoi:\033[m '
      '\033[2;32;40m{}\033[m'.format(n2) )
