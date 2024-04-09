lado1=float(input('\033[1;36;mDigite um número: '))

lado2=float(input('Digite outro número: '))

lado3=float(input('Digite mais outro número: '))

if lado1<lado2+lado3:

    if lado2<lado1+lado3:

        if lado3<lado1+lado2:

            if lado2==lado3:

                if lado1==lado2:

                    print('Triângulo equilátero')

                elif lado1==lado2 or lado1==lado3 or lado2==lado3:

                    print('Triâgulo isóceles')

                else:

                    print('Triângulo escaleno')

            elif lado1==lado2 or lado1==lado3 or lado2==lado3:

                print('Triâgulo isóceles')

            else:

                print('Triângulo escaleno')

        else:

            print('Não foi possível criar um triângulo. Por favor tente novamnte')

    else:

        print('Não foi possível criar um triângulo. Por favor tente novamnte')

else:

    print('Não foi possível criar um triângulo. Por favor tente novamnte')




