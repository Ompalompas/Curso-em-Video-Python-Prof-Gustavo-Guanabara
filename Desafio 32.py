ano=int(input('\033[1;32;41mDigite o ano:\033[m '))

bissexto=ano%4

if bissexto==0:

    print('\033[1;32;41mAno bissexto\033[m')

else:

    print('\033[1;32;41mAno normal\033[m')



