anonasc=int(input('\033[1;33;mAno de nascimento: '))

idade=2018-anonasc

print(idade)

if idade==18:

    print('Apto. Iniciando processo de alistamento...')

elif idade<18:

    print('Falta(m) {} ano(s) para você se alistar.'.format(18-idade))

else:

    print('Você perdeu o prazo para alistamento. Processando multa...')
