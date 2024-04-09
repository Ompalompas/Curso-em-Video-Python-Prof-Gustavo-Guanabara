altura=float(input('\033[1;32;mDigite sua altura: '))

peso=float(input('Digite seu peso: '))

imc=peso/(altura**2)

print(imc)

if imc<18.5:

    print('Você está à baixo do peso')

elif imc<25:

    print('Você está em forma')

elif imc<30:

    print('Você está com sobrepeso')

elif imc<40:

    print('Você está obeso')

else:

    print('Obesidade mórbida')