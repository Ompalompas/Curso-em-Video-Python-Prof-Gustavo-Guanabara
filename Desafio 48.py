#for n in range(1,501,2):
    #if n%3==0:
        #print(n, end=' ')

soma=0
cont=0
cont1=0
for n in range(1,501,2):
    if n%3==0:
        soma+=n
        cont+=1
    #cont1=cont1+1
print('A soma de todos os {} valores solicitados é {}'.format(cont,soma))
#print(cont1)

