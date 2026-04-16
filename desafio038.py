n1=int(input('Primeiro numero: '))
n2=int(input('Segundo numero: '))
if n1 > n2:
    print('O primeiro valor é \033[30;42mMAIOR\033[m')
elif n1 < n2:
    print('O segundo valor é \033[30;42mMAIOR\033[m')
else:
    print('Não existe valor maior, os dois são \033[0;30;41mIGUAIS\033[m')
