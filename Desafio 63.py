n=int(input('Digite a quantidade de termos: '))
t1=0
t2=1
t4=0
cont=3
print('{} → {}'.format(t1,t2), end=' ')
while cont<=n:
    t3=t1+t2
    t4 += t3
    print(' {} → {} → '.format(t3,t4), end=' ')
    cont+=1

