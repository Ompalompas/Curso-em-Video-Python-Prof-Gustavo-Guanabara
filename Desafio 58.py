from random import choice

pc=[1,2,3,4,5,6,7,8,9,10]
venceu=0
perdeu=1

while venceu==0:
    sorteado = int(choice(pc))
    jogador=int(input('Digite um número: '))
    print('###{}ª tentativa###'.format(perdeu))
    if jogador==sorteado:
        print('Você venceu! O número sorteado foi {}'.format(sorteado))
        venceu+=1


    else:
        print('Você perdeu! Tente novamente! O número sorteado foi {}'.format(sorteado))
        perdeu+=1

print('Você precisou de {} tentativas'.format(perdeu))