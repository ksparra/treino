import random
from time import sleep
print('-'*30)
print('tente acertar o número que vou escolher')
print('-'*30)
num = random.randint(0,5)
sorte = int(input('chute um número de 0 a 5 :'))
print('Processando...')
sleep(3)
if num == sorte:
    print(f'o número escolhido foi {num}')
    print('você acertou parabens ')
else:
    print(f'parece que voce errou ')
    print(f'o número escolhdo foi {num}')
print('-'*30)
print('BOM JOGO')
print('-'*30)
