import random
num = random.randint(0, 5)
n1 = int(input('Digite um numero de 0 a 5: '))
if n1 == num:
    print('Voce acertou!PARABÉNS')
else:
    print('Voce errou! Tente de novo')
    print(f'Seu número foi: {n1}')