import random

jogador=input('\033[;32;mPedra, papel ou tesoura? ').lower()

lista=['pedra','papel','tesoura']

comp=random.choice(lista)

print(comp)

if jogador=='pedra':

    if comp=='tesoura':

        print('Você ganhou!')

    else:

        print('Você perdeu! Tente novamente')

elif jogador=='papel':

    if comp=='pedra':

        print('Você ganhou!')

    else:

        print('Você perdeu! Tente novamente')

elif jogador=='tesoura':

    if comp=='papel':

        print('Você ganhou!')

    else:

        print('Você perdeu! Tente novamente')

else:

    print('Você perdeu! Tente novamente')



