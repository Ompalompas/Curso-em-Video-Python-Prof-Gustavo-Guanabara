from random import randint
v=0
while True:
    jogador=int(input('Digite um valor: '))
    computador=randint(0,10)
    total=jogador+computador
    tipo=' '
    while tipo not in 'PI':
        tipo=str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total}',end=' ')
        print(f'DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo=='P':
        if total % 2 == 0:
            print('Você venceu!')
            v+=1
        else:
            print('Você perdeu!')
            break
    elif tipo=='I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!!! Você venceu {v} vezes')





'''from random import randint
while True:
    jogador=int(input('Digite um número: '))
    computador=randint(0, 10)
    total=jogador+computador
    tipo=' '
    while tipo not in 'PI':
        tipo=str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
        print(f'Você jogou {jogador} e o computador {computador}. Total: {total}')
        if tipo == 'P':
            if total % 2 == 0:
                print('Você venceu! Foi sorteado um número par')
            else:
                print('Você perdeu. Foi sorteado um número ímpar')
        if tipo == 'I':
            if total % 2 == 1:
                print('Você venceu! Foi sorteado um número ímpar')
            else:
                print('Você perdeu. Foi sorteado um número par')'''
