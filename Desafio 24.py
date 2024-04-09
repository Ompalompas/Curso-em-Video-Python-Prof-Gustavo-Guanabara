##Desafio 24
n1=(input('\033[1;33;40mEm\033[m \033[1;33;mqual\033[m \033[1;30;44mcidade\033[m '
'\033[1;;45mvocê\033[m \033[1;30;46mnasceu?\033[m')).strip()

#n2=n1.strip().lower().split()
#print('Sua cidade começa com a palavra Pernambuco? ','pernambuco' in n2[0])

print(n1[:10].lower()=='pernambuco')