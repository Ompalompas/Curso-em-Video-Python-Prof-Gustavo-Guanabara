#Mundo 3 do curso de Python
#Estrutura de repetição while
#while not apple
    #passo
#pega

#################################################################################

'''
c=1
while c<10:
    print(c)
    c+=1
print('FIM')

##################################################################################

n=1
while n != 0:
    n=int(input('Digite um valor: '))
print('Fim')

###################################################################################

r='S'
while r =='S':
    n=int(input('Digite um valor: '))
    r=str(input('Quer continuar?[S/N] ').upper())
print('############## FIM ##############')

#####################################################################################
num=1
par=impar=0
while num != 0:
    num=int(input('Digite um número: '))

    if num!=0:
        if num%2==0:
            par+=1
        else:
            impar+=1

print('Foram {} números pares e {} números ímpares'.format(par,impar))
'''

r=0

while r==0:
    sexo=str(input('Digite o sexo [M/F]: ').upper())

    if sexo == 'M':
        r +=1
        print('Informações válidas!')


    elif sexo=='F':
        r+=1
        print('Informações válidas!')

    else:
        print('Informações digitadas estão incorretas')



