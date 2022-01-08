tot = 0
tot1 = 0
num2 = 0
while not num2 > 999:

    num1 = int(input('digite um número [999 para parar]  :'))
    tot1 += 1

    if num2 < 999:
        num2 = num2 + num1

num3 = num2 - 999
print(f'voce digitou {tot1-1} valores o valor junto é {num3}')