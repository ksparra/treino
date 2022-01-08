from random import choice
print('sua as opçoões :')
print('[1] pedra')
print('[2] papel')
print('[3] tesoura')
jogador = int(input('Qual sua opção :'))

lista = [1,2,3]
computado = choice(lista)

if jogador >=4 :
    print('jogada invalida')
elif jogador == 3 and computado == 2 or jogador == 2 and computado == 1 or jogador == 1 and computado == 3:
    print('o jogador vençeu ')
    print(f'o jogador escolheu {jogador} e o computador {computado}')
elif jogador == computado:
    print('o jogo deu empate ')
    print(f'o jogador escolheu {jogador} o computador {computado}')