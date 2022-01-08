num = int(input('digite o valor : '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'o número analisado é {num}')
print(f'a unidade do número {num} é {u}')
print(f'o decimal do número {num} é {d}')
print(f'a centena do número {num} é {c}')
print(f'o milenio do número {num} é {m}')

