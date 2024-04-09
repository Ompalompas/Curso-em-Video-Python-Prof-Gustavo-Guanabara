''''Tuplas, Listas e dicionários
Variáveis simples e compostas

As tuplas são imutáveis
'''

#lanche='Hambúrguer', 'Suco', 'Pizza', 'Pudim'
#print(lanche[-3:])
##lanche[0]='refrigerante' tuplas são imutáveis depois da sua primeira atribuição

#print(lanche)
#print(lanche[3])
#print(lanche[-2])
#print(lanche[1:3]) ==> nesse caso desconsidera o 3. mostrando 1 e 2
#print(lanche[2:])
#print(lanche[:2])
#print(lanche[-3:])


''' EXEMPLO 1:

lanche=('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
'''

''' EXEMPLO 2: (Mesmo resultado do ex1 feito de outra maneira)

lanche=('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!')
'''

'''EXEMPLO 3:

lanche=('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
'''

''' EXEMPLO 4:

lanche=('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(sorted(lanche)) ###Coloca em ordem alfabética!
print(lanche)

'''

'''EXEMPLO 5:

a=(2,5,4)
b=(5,8,1,2)
c=b+a     ### Observe que nesse caso a+b não é igual a b+a
print(c)

'''

'''EXEMPLO 6:
a=(2,5,4)
b=(5,8,1,2)
c=b+a
print(len(c))
'''


'''EXEMPLO 7:
a=(2,5,4)
b=(5,8,1,2)
c=b+a
print(c.count(5)) ### Quantas vezes está aparecendo o número 5 em c

'''

'''EXEMPLO 8:
a=(2,5,4)
b=(5,8,1,2)
c=b+a
print(c)
print(c.index(4)) ### Mostra em qual posição está determinado elemento
'''

'''EXEMPLO 9:
a=(2,5,4)
b=(5,8,1,2)
c=b+a
print(c)
print(c.index(2,4)) ### Mostra em qual posição está o número 2 contando a partir do 4 elemento
'''

'''EXEMPLO 10:
a=(2,5,4)
b=(5,8,1,2)
c=b+a
print(c)
print(c.index(5,1))
'''
'''EXEMPLO 11
pessoa=('Gustavo', 39, 'M', 99.88)
del(pessoa) ### Apaga da memória. Só é possível apagar a tupla inteira. Não é possível deletar apenas 1 item
print(pessoa)
'''
'''EXEMPLO 12
pessoa=('Gustavo', 39, 'M', 99.88)
print(pessoa)
'''


contagem=('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
          'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero=0
while True:
    numero=int(input('Digite um número de 0 a 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente! ',end='')
print(f'Você digitou o número: {contagem[numero]}')

