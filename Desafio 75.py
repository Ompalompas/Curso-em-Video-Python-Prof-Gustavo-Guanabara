num=(int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')))

print(f'O número 9 foi digitado {num.count(9)} vezes')

if 3 in num:
    print(f'O primeiro número 3 está na {num.index(3)+1} posição')
else:
    print('Não foi digitado o número 3')

print(f'Números pares: ', end='')

for c in num:
    if c%2==0:
        print(c, end=' ')