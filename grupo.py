import datetime
ano = datetime.date.today().year
tot = 0
totmaior = 0
for c in range(1, 7):
    tot += c
    vei = int(input(f'em que ano a {c} nasceu :'))
    idade = ano - vei
    if idade >= 18:
        print('vei')
    elif idade <= 17:
        print('criança')
    else:
        print('número invalido')
    if idade >= 18 :
        totmaior += 1
    else:
        tot +=1
print(f'quantidade de pessoas velhas {totmaior}')
print(f'quantidade de crainça {tot}')



