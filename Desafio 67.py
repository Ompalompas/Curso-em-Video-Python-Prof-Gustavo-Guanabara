while True:
    num=int(input('Quer ver a tabuada de qual número?'))
    print('-'*30)
    if num<0:
        break
    for c in range(1,11):
        print(f'{num} X {c} = {num*c}')
        n=num
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO')
