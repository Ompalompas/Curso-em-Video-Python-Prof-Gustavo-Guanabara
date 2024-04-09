#Desafio 10
var1=float(input('\033[7;33;40mDigite\033[m \033[7;34;40mo '
'valor\033[m \033[7;34;40mem\033[m \033[7;35;40m reais: R$\033[m'))
var2=var1/3.27
print('Equivalente à: ${:.2f} dólares na cotação atual'.format(var2))
