casa = float(input('Qual o valor da casa?: '))
salario = float(input('Qual é o salário?: '))
anos = int(input('Quantos anos de financiamento?: '))
meses = anos * 12
prestacao = casa / (anos * 12)
if prestacao > salario * 30 / 100:
    print('O valor da sua prestação é {} NEGADO!'.format(prestacao))
else:
    print(' O valor da sua prestação é {} APROVADO!'.format(prestacao))



