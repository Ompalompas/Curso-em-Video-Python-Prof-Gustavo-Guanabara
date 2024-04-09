soma=0
cont=0
for c in range(1,7):
    n1=int(input('Digite um número inteiro: '))
    if n1%2==0:
        cont+=1
        soma+=n1
print('A soma de todos os {} números pares é: {}'.format(cont,soma))