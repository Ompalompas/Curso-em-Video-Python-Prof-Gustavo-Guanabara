print('GERADOR DE P.A.')
print(10*'=-')

primeiro=int(input('Primeiro termo: '))

razão=int(input('Razão: '))

termo=primeiro

c=1

mais=10

total=0


while mais != 0:
    total+=mais

    while c <= total:

        print('{} →'.format(termo), end=' ')
        termo+=razão
        c+=1

    print('PAUSA')

    mais=int(input('\nMais quantos termos você gostaria de ver? '))

print('Progressão finalizada com {} termos mostrados'.format(total))