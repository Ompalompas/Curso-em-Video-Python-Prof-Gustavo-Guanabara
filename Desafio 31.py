kmviagem=float(input('\033[1;34;mDigite quantos km foram percorridos:\033[m '))

if kmviagem<=200:

    print('\033[1;34;mValor da passagem: R${:.2f}\033[m'.format(kmviagem*0.5))

else:

    print('\033[1;34;mValor da passagem: R${:.2f}\033[m'.format(kmviagem*0.45))
