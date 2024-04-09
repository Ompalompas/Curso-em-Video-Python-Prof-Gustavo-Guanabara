#Desafio 13
salario=int(input('\033[7;30;45mDigite\033[m \033[7;30;46mo valor'
'\033[m \033[7;30;47mdo seu\033[m \033[7;31;42msalário\033[m'
' \033[7;30;41matual:\033[m'))
aumento=salario/100*15
salarionovo=salario+aumento
print('Parabéns! Você recebeu um aumento de R${:.0f}, seu novo salário é R${:.0f}'.format(aumento,salarionovo))

