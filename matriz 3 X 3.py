lista1 = [[], [], []]
pilha = []
valor = 0
tot1 = 0
tot2 = 0
cont = 0
for c in range(0, 9):
    valor = int(input(f'Digite um valor para [{tot1,tot2}]:'))

    lista1[tot1].append(valor)
    tot2 += 1

    cont += 1

    if cont == 3:
        tot1 += 1
        tot2 -= 3
        cont -= 3
print('-=-'*10)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista1[l][c]:^5}]',end='')
