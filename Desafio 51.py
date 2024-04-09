#num = int(input('\nDigite o Primeiro número da PA: '))
#razão = int(input('Digite a Razão da PA: '))
#for c in range(1, 11):
    #print(num, end=' ')
    #num += razão
#print('Acabou')

#a1=int(input('Digite o primeiro termo da P.A.: '))
#r=int(input('Digite a razão: '))
#for n in range(0,10):
    #a2=a1+n*r
    #print('{} termo da P.A.: {}'.format(n+1,a2))

primeiro=int(input('Primeiro termo: '))

razão=int(input('Razão: '))

décimo=primeiro+(11-1)*razão #fórmula para calcular o décimo termo de uma P.A(enésimo termo, neste caso o numero 10)

for c in range(primeiro,décimo,razão):  #décimo+razão

    print('{} '.format(c), end=' ')

print('ACABOU')