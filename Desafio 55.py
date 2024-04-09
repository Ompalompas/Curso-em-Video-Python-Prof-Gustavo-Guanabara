#Estudar sobre análise de dados
maior=0
menor=0
for p in range(1,6):
    peso = int(float(input('Peso da {}ª pessoa: '.format(p))))
    if p==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso

        if peso<menor:
            menor=peso

print('O mais pesado foi: {}Kg e o mais leve foi: {}Kg '.format(maior,menor))



