import random
tot = 0
num = random.randint(0, 10)
print('acabei de pensar em um número entre 0 a 10 chute porfavor :')
acertou = False
while not acertou:
    jogador = int(input('seu palpite'))
    tot+= 1
    if jogador > num:
       print('um pouco menor :')

    if jogador < num:
       print('um pouco maior :')

    if jogador == num:
        acertou = True

print(f'acerto em {tot} tentativas')
