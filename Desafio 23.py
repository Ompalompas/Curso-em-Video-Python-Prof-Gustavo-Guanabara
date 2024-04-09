#Desafio 23
#n =(input('Informe um número: '))
#print('Analisando o número {}'.format(n))
#print('Unidade: {}'.format(n[3]))
#print('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))


num =int(input('\033[1;31;45mInforme\033[m \033[1;31;46mum\033[m '
'\033[1;31;47mnúmero:\033[m '))

n = str(num)
unidade=num//1%10
dezena=num//10%10
centena=num//100%10
milhar=num//1000%10

print('\033[1;32;mAnalisando\033[m \033[1;32;40mo\033[m \033[1;32;41mnúmero\033[m'
' \033[1;32;m{}\033[m'.format(num))

print('\033[1;32;40mUnidade:\033[m \033[1;32;m{}\033[m'.format(unidade))

print('\033[1;32;mDezena:\033[m \033[m \033[1;32;40m{}\033[m'.format(dezena))

print('\033[1;32;mCentena:\033[m \033[1;33;m{}\033[m'.format(centena))

print('\033[1;33;40mMilhar:\033[m \033[1;33;41m{}\033[m'.format(milhar))