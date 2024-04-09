n1=float(input('\033[1;30;43mDigite um número:\033[m '))

n2=float(input('\033[1;30;43mDigite outro número:\033[m '))

n3=float(input('\033[1;30;43mDigite mais um número:\033[m '))

if n1>n2:

    maior1=n1

    menor1=n2

else:

    maior1=n2

    menor1=n1

if maior1>n3:

    print('\033[1;30;43mNúmero maior:\033[m {:.3f}'.format(maior1))

    if menor1<n3:

        print('\033[1;30;43mNúmero menor:\033[m {:.3f}'.format(menor1))

    else:

        print('\033[1;30;43mNúmero menor:\033[m {:.3f}'.format(n3))

else:

    print('\033[1;30;43mNúmero maior:\033[m {:.3f}'.format(n3))

    if n3<menor1:

        print('\033[1;30;43mNúmero menor:\033[m {:.3f}'.format(n3))

    else:

        print('\033[1;30;43mNúmero menor:\033[m {:.3f}'.format(menor1))