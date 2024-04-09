continuar=' '
total=0
maisdemil=0
maisbarato=0
nomedomaisbarato=' '

while continuar not in 'N':

    produto=input('Nome do produto: ')
    preço=float(input('Preço: '))
    continuar=input('Deseja continuar? [S/N]: ').strip().upper()
    total+=preço


    if preço<maisbarato:
        nomedomaisbarato=produto

    if maisbarato == 0:
        maisbarato = preço

    if preço>1000:
        maisdemil+=1

print(f'O total da compra foi R${total}.', end=' ')
print(f'{maisdemil} produtos custaram mais de mil reais', end=' ')
print(f'Produto mais barato: {nomedomaisbarato}')
