ced=50
total=0
valor=int(input('Valor do saque: '))
total=valor
totaldeced=0

while True:
    if total>=ced:
        total-=ced
        totaldeced+=1
    else:
        print(f'Cédulas de {ced}: {totaldeced}')
        totaldeced=0
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        if total==0:
            break












