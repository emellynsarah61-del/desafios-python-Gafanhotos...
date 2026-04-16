n = int(input('Escolha um número inteiro: '))
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
opcao = int(input('Sua Opção: '))
n1 = bin(n)
n2 = oct(n)
n3 = hex(n)
if opcao == 1:
    print('O escolhido foi {}'.format(n1[2:]))
elif opcao == 2:
    print('O escolhido foi {}'.format(n2[2:]))
elif opcao == 3:
    print('O escolhido foi {}'.format(n3[2:]))
else:
    print('Opção inválida!')
