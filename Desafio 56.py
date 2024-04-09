somadasidades=0
maisvelho=0
nomedomaisvelho=0

for c in range(1,5):
    print('### {} PESSOA ###'.format(c))
    nome=str(input('nome: ')).strip()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo: ')).strip()
    somadasidades+=idade

    if c==1 and sexo in 'Mm':
        maisvelho=idade
        nomedomaisvelho=nome

    if sexo in 'Mm' and idade>maisvelho:
        maisvelho=idade
        nomedomaisvelho=nome

print('{} tem {} anos e é o mais velho'.format(nomedomaisvelho,maisvelho))



