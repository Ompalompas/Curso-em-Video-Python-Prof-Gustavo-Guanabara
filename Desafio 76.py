print('-'*40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-'*40)

produtos=('cadeira',30,'mesa',100,'ventilador',50,'geladeira',700, 'liquidificador', 80, 'fogao', 400, 'perfume',150,'luminária',40,'colchão',300,'prato', 10)

for posicao in range(0,len(produtos)):

    if posicao%2==0:

        print(f'{produtos[posicao]:.<30}',end=' ')

    else:

        print(f'R${produtos[posicao]:>5.2f}')

print('-'*40)