s = True
tot = 0
while tot < 10:
    num1 = int(input('Digte o valor da tabuada :'))
    if num1 < 0:
        break
    print('-'*30)

    if num1 > 0:
        for c in range(1, 11):
            res = num1 * c
            print(f'{num1} x {c} = {res}')








