n1 = int(input('calcule o fatorial'))
c = n1
f = 1
print('calculando ')
while c >0:
    print(f'{c}'),
    print('x'if c > 1 else '=')
    f = f * c
    c -= 1
print(f'o faorial de {n1} é {f}')