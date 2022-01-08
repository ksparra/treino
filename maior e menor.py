s = False
tot = 0
tot2 = 0
maior = 0
menor = 0
tot3 = 0
while s == False:
    num1 = int(input('Digite um número :'))
    sn = str(input('Quer continuar [S/N] :'))

    tot3 += 1

    if tot3 == 1:
        menor = maior = num1
    else:
        if num1 > maior:
            maior = num1
        if num1 < menor:
            menor = num1

    if num1 > 0:
        tot += 1

    if num1 > 0:
        tot2 = num1 + num1

    if sn == 'Nn':
        s = True

obj = tot2 / tot

print(f'voce digitou {tot} números e a mèdia foi {obj} o maior valor foi {maior} e o menor {menor}')
