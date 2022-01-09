print('='*20)
print('       BANCO')
print('='*20)

cinquenta = 50

quanto = int(input('quanto vc quer sacar :'))

ced = 0

total = quanto

while True:
    if total >= cinquenta:
        total -= cinquenta
        ced += 1
    else:
        print(f'total de {ced} cédulas de R$ {cinquenta}')
        if cinquenta == 50:
            cinquenta = 20

        elif cinquenta == 20:
            cinquenta = 10

        elif cinquenta == 10:
            cinquenta = 5

        elif cinquenta == 5:
            cinquenta = 1

        ced = 0

        if total == 0:
            break
