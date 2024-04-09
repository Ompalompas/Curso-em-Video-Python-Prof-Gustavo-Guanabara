dtnasc=int(input('\033[1;34;40mAno de nascimento:'))

idade=2018-dtnasc

print(idade)

if idade<=9:

    print('Categoria Mirim')

elif idade<=14:

    print('Categoria Infantil')

elif idade<=19:

    print('Categoria Junior')

elif idade<=20:

    print('Categoria Sênior')

else:

    print('Categoria Master')



