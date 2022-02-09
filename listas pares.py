principal = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input(f'Digite o valor{c}'))

    if valor % 2 == 0:
        principal[0].append(valor)
    else:
        principal[1].append(valor)
print('-=-'*20)
principal[0].sort(reverse=False)

print(f'o valores parres são {principal[0]}')
principal[1].sort(reverse=False)    

print(f'o valor impar são {principal[1]}')

