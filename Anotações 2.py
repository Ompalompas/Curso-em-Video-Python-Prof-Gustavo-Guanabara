#nome = str(input('Qual é o seu nome?'))
#if nome=='Gustavo'
   #print('Que nome bonito!') ##Estrura condicional simples
#print('Tenha um bom dia, {}!'.format(nome))

#nome = str(input('Qual é o seu nome?'))
#if nome=='Gustavo'
   #print('Que nome bonito!')
#else:
    #print('Seu nome é bem normal') ##Estrutura condicional composta
#print('Tenha um bom dia, {}!'.format(nome))


nome = str(input('\033[1;30;mQual é o seu nome? ')).lower()
if nome=='gustavo':
   print('Que nome bonito!')

elif nome=='pedro' or nome=='maria' or nome=='paulo':
    print('Seu nome é bem popular no Brasil')  ##Estrutura aninhada

#O elif pode ser utilizado quantas vezes quiser

elif nome in 'ana claudia jéssica juliana':
    print('Belo nome feminino')

else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))



