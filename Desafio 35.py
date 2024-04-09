lado1=float(input('\033[1;32;mDigite o primeiro comprimento:\033[m '))

lado2=float(input('\033[1;32;mDigite o segundo comprimento:\033[m '))

lado3=float(input('\033[1;32;mDigite o terceiro comprimento:\033[m \033[1;32;m'))

if lado1<lado2+lado3:

    if lado2<lado1+lado3:

        if lado3<lado1+lado2:

            print('Triângulo criado com sucesso!')

        else:

            print('Não foi possível criar um triângulo, '
                  'por favor tente novamente')

    else:

        print('Não foi possível criar um triângulo, '
              'por favor tente novamente')

else:

    print('Não foi possível criar um triângulo, '
          'por favor tente novamente.')
