
#Exemplo 1:
'''

cont = 1
while cont <= 10:
    print(cont,'-> ', end='')
    cont += 1
print('Acabou')

'''


#Exemplo 2: (Looping infinito)

'''
cont = 1
while True:
    print(cont,'-> ', end='')
    cont += 1
print('Acabou')

'''


#Exemplo 3:

'''

n = 0
while n != 999:
    n = int(input('Digite um número: '))

'''


#Exemplo 4:

'''

n = cont = 0
while cont < 5:
    n = int(input('Digite um número: '))
    cont += 1

'''


#Exemplo 5:

'''

n = cont = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
print(f'A soma é: {soma}')

'''


#Exemplo 6:

'''

nome = 'José'
idade = 32

print(f'O {nome} tem {idade} anos') #PYTHON 3.6+
print('O {} tem {} anos'.format(nome,idade)) #PYTHON 3
print('O %s tem %d anos' % (nome,idade)) #PYTHON 2

'''


#Exemplo 7:

'''

nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome:=^20} tem {idade:*^20} anos e ganha R${salario:.2f}')

'''

soma=cont=0
while True:
    num=int(input('Digite um número: '))
    if num==999:
        break
    soma+=num
    cont+=1
print(f'A soma dos {cont} valores digitados é: {soma}')










