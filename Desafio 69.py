resposta = ' '
demaior=0
homens=0
mulheres=0
while resposta not in 'N':
    idade=int(input('Idade: '))
    sexo=input('Sexo: [M/F] ').strip().upper()[0]
    resposta=input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if idade>=18:
        demaior+=1
    if sexo=='M':
        homens+=1
    if sexo=='F':
        if idade<20:
            mulheres+=1

print(f'{demaior} cadastrados são de maior, {homens} homens e {mulheres} mulheres tem menos de 20 anos')





