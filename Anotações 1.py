#nome = input('Qual seu nome? ')
#print('Prazer em te conhecer',nome,'!')

#n1=int(input('Digite um número: '))
#n2=int(input('Digite mais um Número: '))
#s=n1+n2
#print('A soma é: ',s)

#n1 = int(input('Digite um valor: '))
#n2 = int(input('Digite um valor: '))
#s = n1+n2
#print('A soma vale entre',n1,'e',n2,'é:',s)

#print ('A soma entre {} e {} é igual a {}'.format(n1,n2,s))

#print(type(n1))

#Principais tipo primitivos: int (ex: 7,-4,0,9875)
#float (ex 4.5, 0.076, -15.223, 7.0)
#bool (ex True, False)
#str ('Olá', '7.5','')
#str já vem padrão

#n1 = input('Digite algo: ')
#print(n1.isnumeric())
#n1.is
#.isnumeric = ver se é um valor com o tipo primitivo int
#.isalpha = ver se é alfabeto
#.isalnum = ver se é alfanumérico
#.isupper = ver se é letra maiúscula
#.islower = ver se é letra minúscula

#print('='*40)
#var1 = input('Digite alguma coisa: ')
#print('='*40)
#print('É um número?: ',var1.isnumeric())
#print('='*40)
#print('É alfanumérico?: ',var1.isalnum())
#print('='*40)
#print('É alfabeto?: ',var1.isalpha())
#print('='*40)
#print('É decimal?: ',var1.isdecimal())
#print('='*40)
#print ('É um dígito?: ',var1.isdigit())
#print('='*40)
#print ('É maiúsculo?: ',var1.isupper())
#print('='*40)
#print ('É minúsculo?: ',var1.islower())
#print('='*40)
#print ('É identifier?: ',var1.isidentifier())
#print('='*40)
#print ('Pode ser impresso?: ', var1.isprintable())
#print('='*40)
#print ('É espaço?: ', var1.isspace())
#print('='*40)
#print ('É um título?: ', var1.istitle())
#print('='*40)
#print ('É um init subclass: ', var1.__init_subclass__())
#print('='*40)

#var1 = input('Digite alguma coisa: ')
#print ('É um número?: ',var1.isnumeric(),' É alfanumérico?: ',var1.isalnum(),
#' É alfabeto?: ',var1.isalpha(),' É decimal?: ',var1.isdecimal(),' É um dígito?: ',
#var1.isdigit(),' É maiúsculo?: ',var1.isupper(),' É minúsculo?: ',var1.islower(),
#' É identificado?: ',var1.isidentifier(),' Pode ser impresso?: ', var1.isprintable(),
#' É espaço?: ', var1.isspace(),' É um título?: ', var1.istitle(),
#' É um init subclass: ', var1.__init_subclass__())

#Operadores:
# + = adição 5+2=7
# - = subtração 5-2=3
# * = multiplicação 5*2=10
# / = divisão 5/2=2.5
# ** = potência 5**2=25
# // = divisão inteira 5//2=2
# % = módulo, resto da divisão 5%2=1

#Ordem de precedência
#1=()
#2= **
#3= *   /   //   %      (resolve quem aparecer primeiro)
#4= +   -               (resolve quem aparecer primeiro)

#Raiz quadrada eleva a potência por meio ex: 81**(1/2)
#Raiz cúbica ex: 25**(1/3)

#print('='*20)

#var1=int(input('Digite um número: '))
#var2=int(input('Digite outro número: '))
#var3= (var1+var2)
#var4= (var1-var2)
#var5= (var1*var2)
#var6= (var1/var2)
#var7= (var1**var2)
#var8=(var1//var2)
#var9= (var1%var2)

#print('A soma é {:.3f}, o produto é {:.3f} e a divisão é {:.3f}'.format(var1, var5, var6))
#print('A subtração é {}, a potência é {}, a divisão inteira é {}, o módulo é {}'.format(var4,var7,var8,var9))

#{:.3f} = 3 pontos flutuantes além da vírgula
#end=' ' = não divide a linha (ex: end='>>>>')
#/n nova linha


#print('O primeiro {} mais o segundo {} é igual à: {}'
#.format (var1,var2,var3))
#print ('O primeiro {} menos o segundo {} é igual à: {}'.format(var1,var2,var4))
#print ('O primeiro {} vezes o segundo {} é igual à: {}'.format(var1,var2,var5))
#print ('O primeiro {} dividido pelo segundo {} é igual à: {}'.format(var1,var2,var6))
#print ('A potência {} do primeiro pelo segundo {} é igual à: {}'.format(var1,var2,var7))
#print ('A divisão inteira do primeiro {} pelo segundo {} é igual à: {}'.format(var1,var2,var8))
#print ('O módulo do primeiro {} pelo segundo {} é igual à: {}'.format(var1,var2,var9))

#nome=input('Primeiro nome: ')
#print('Bem-vindo {:<20}!' .format(nome))

#print('Bem-vindo {:20}!' .format(nome)) quantidade de
#espaços disponíveis para ser digitado
# ^ = texto centralizado
# > = à direita
# < = à esquerda

#+
#-
#*
#**
#/
#//
#%

#n1=int(input('digite um numero: '))
#n2=int(input('digite mais um número: '))
#print('A soma vale {}'.format(n1+n2))
#s=n1+n2 utiliza variável quando ainda vai se precisar
#do valor, nesse caso foi apenas jogado na tela

#import emoji
#print(emoji.emojize('Olá mundo!:heart_eyes:', use_aliases=True))

#import random
#num = random.random()
#print(num)

#num=random.randint(1,10)
#print(random.random)

#ctrl+espaço = mostra as possibilidades
#import math = importação biblioteca completa

#from math import sqrt,floor,ceil,acos
#num=int(input('Digite um número: '))
#raiz= math.sqrt(num)
#print('A raiz de {} é igual à {}'.format(num,math.floor(raiz)))

#print('A raiz de {} é igual à {:.2f}'.format(num,raiz))

#Utilizando módulos:
#import math
#from math import sqrt, ceil
#ceil = arredonda para cima
#floor = arredonda para baixo
#trunc = elimina da vírgula para frente sem arredondar
#pow = potência, funciona semelhante à **
#sqrt = square root, raiz quadrada
#factorial = calcula número fatorial
#python.org = estudar linguagem

##Manipulando textos
##Fatiamento de string
# frase[9]
# frase[9:13]
# frase[9:21:2]
# frase[:5]
# frase[15:]
# frase[9::3]
# len(frase) = comprimento da frase
# frase.count('o') = quantas vezes aparece a letra "o"
# frase.count('o',0,13)
# frase.find('deo')
# frase.find('Adroid')
# 'curso' in frase

##Transformação
# frase.replace('Python', 'Android') = substitui um pelo outro
# frase.upper()
# frase.lower()
# frase.capitalize() = deixa tudo em minusculo menos a primeira letra
# frase.title() = captalize em todas as palavras
# frase.strip() = remove espaços excedentes
# frase.rstrip() = remove espaços da direita
# frase.lstrip() = remove espaços da esquerda
# frase.split() = dividir string em uma lista e listar os elementos
# '-'.join(frase)

# print(""" """) = concatena várias linhas

# frase = 'Curso em Vídeo Python'
# print(frase[::2])
# print(frase.count('o'))
# print(frase.upper().count('O'))
# print(len(frase.strip()))
# print(frase.replace('Python','Android'))
# print(frase[0])
# print('Curso' in frase)
# print(frase.find('Vídeo'))
# print(frase.lower().find('vídeo'))
# print(frase.split())
# dividido=frase.split()
# print(dividido[2][3])

#Fórmula fatiar utilizando a matemática:
#unidade=num//1%10
#dezena=num//10%10
#centena=num//100%10
#milhar=num//1000%10

#10 estrutura condicional
#Condição simples, compostas e simplificadas

#if carro.esquerda():
#bloco True
#else:
#bloco False

#tempo=int(input('Quantos anos tem seu carro?'))
#print('carro novo' if tempo<=3 else 'carro velho' )
#print('--FIM--')

#tempo=int(input('Quantos anos tem seu carro?'))
#if tempo<=3:
    #print('carro novo')
#else:
    #print('carro velho')
#print('--FIM--')

#nome=str(input('Qual é seu nome? '))
#if nome=='Gustavo':
    #print('Que nome lindo você tem!')
#else:
    #print('Seu nome é tão normal!' )
#print('Bom dia {}!'.format(nome))

#n1=float(input('Digite a primeira nota: '))
#n2=float(input('Digite a segunda nota: '))
#m=(n1+n2)/2
#print('A sua média foi {:.1f}'.format(m))
#if m>=7.0:
    #print('Sua média foi boa parabéns!')
#else:
    #print('Sua média foi ruim! Se esforce mais da próxima vez!')
#print('PARABÉNS' if m>=7 else 'ESTUDE MAIS')

#ANSI - Escape Sequence
# \033[ códigodacor m
# \033[ style, cor do texto, cor do background m

#Style 0=None ou nada, 1=negrito, 4=underline,
#7=inverte as configurações

#Text 30 até 37

#Background 40 até 47

#\033[;30;41m
#\033[4;33;44m
#\033[1;35;43m
#\033[30;42m
#\033[m
#\033[7;30m

#Pesquisar modo colorize













