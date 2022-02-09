num = list()
tot = 0
while True:

    num2 = int(input('Digite um valor :'))
    num.append(num2)
    tot += 1
    sn = str(input('Você quer continuar [S/N]:')).upper()

    if 'N' in sn:
        break
    if sn not in 'Ss''Nn':
        print('invalido')
        break
num.sort(reverse=True)

print('-=-'*10)
print(f'voce digitou {tot} elementos')
print(f'os valoes em ordem decresente são{num}')
if 5 in num:
    print('o valor 5 faz parte da lista')