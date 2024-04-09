tot=0
núm=int(input('Digite um número inteiro: '))
for c in range(1,núm+1):
    if núm%c==0:
        print('\033[33m', end='')
        tot+=1
    else:
        print('\033[31m',end='')
    print('{} '.format(c), end='')

print('\nO número {} foi divisível {} vezes'.format(núm,tot))

if tot==2:
    print('\033[m{} é um número primo'.format(núm),end='')
else:
    print('\033[m{} não é um número primo'.format(núm),end='')

