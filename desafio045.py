import random
from time import sleep
print('''VAMOS JOGAR! ESCOLHE:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogador = int(input('Sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
jogo = random.randint(1, 3)
itens = ['Pedra', 'Papel', 'Tesoura']
if jogador == jogo:
    print('EMPATE!')
elif (jogador == 1 and jogo == 3) or \
     (jogador == 2 and jogo == 1) or \
     (jogador == 3 and jogo == 2):
    print('VOCÊ GANHOU!')
else:
    print('COMPUTADOR GANHOU!')




