print('{:=^40}'.format('LOJAS ALEATOÓRIAS'))
preco = float(input('Qual o preço do produto? R$: '))
print('''Escolha uma forma de pagamento:
[1] → à vista (10% de desconto)
[2] → à vista no cartão (5% de desconto)
[3] → até 2x no cartão (preço normal)
[4] → 3x ou mais no cartão (20% de juros)''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    vista = preco * 0.90
    print('À vista: R${:.2f}'.format(vista))
elif opcao == 2:
    cartao = preco * 0.95
    print('À vista no cartão: R${:.2f}'.format(cartao))
elif opcao == 3:
    total = preco
    parcela = preco / 2
    print('2x de R${:.2f} (Total: R${:.2f})'.format(parcela, preco))
elif opcao == 4:
    vezes = int(input('Quantas parcelas? '))
    total = preco + (preco * 20 / 100)
    parcela = total / vezes
    print('{}x de R${:.2f} (Total: R${:.2f})'.format(vezes, parcela, total))
else:
    print('OPÇÃO INVÁLIDA!!!!')
print('{:=^40}'.format('FIM DO PROGRAMA!'))
