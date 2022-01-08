import random

print('Vamos jogar um jogo !!!')

jgv = 0
pcv = 0
pc2 = ''

while not pcv + jgv == 3:
    pc = random.randint(1, 100)

    jogador = int(input('escolha um número : '))
    jogador2 = str(input('escolha entre immpar ou par [P/I]: '))

    if jogador2 == 'P':
        pc2 = 'I'
    if jogador2 == 'I':
        pc2 = 'P'

    final = jogador + pc

    print(f'o número foi {final}')

    if final % 2 == 0:
        if jogador2 == 'P':
            jgv = jgv + 1
        if pc2 == 'P':
            pcv = pcv + 1
    else:
        if pc2 == 'I':
            pcv = pcv + 1
        if jogador2 == 'I':
            jgv = jgv + 1

print(f'o jogador teve {jgv} e a maquina teve {pcv} pontos ')
if jgv == 2:
    print('o vencedor é o jogador ')
if pcv == 2:
    print('a maquina venceu ')



