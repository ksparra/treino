import operator
from random import randint
import time
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6),
}
print(f'valores sorteados ')
for k, l in jogo.items():
        print(f'{k} jogou {l}')
        time.sleep(1)
print('-=-'*5)
rankin = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
for v, m in enumerate(rankin):
        print(f'{v+1} lugar :{m[0]} com {m[1]}')
