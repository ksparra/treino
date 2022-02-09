num = list()
nump = list()
numi = list()

while True:
    add = int(input('digite um número:'))
    num.append(add)
    sn = str(input('quer continuar [S/N]:')).upper()

    if add % 2 == 0:
        nump.append(add)
    else:
        numi.append(add)

    if sn not in 'SN':
        print('invalido')
        break

    if 'N' in sn:
        break

print('-=-'*10)
print(f'a lista completa{num}')
print(f'a lista em par{nump}')
print(f'a lista em impar{numi}')

