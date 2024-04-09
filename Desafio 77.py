palavras=('quadro','geladeira','liquidificador','televisao','relogio','mesa','sofa','fogao','panela','armario')

for palavra in palavras:

    print(f'\nNa palavra {palavra.upper()}, temos: ',end='')

    for letra in palavra:

        if letra.lower() in 'aeiou': #Ex: 'aáãàâ' também podem ser utilizados

            print(letra,end=' ')