import datetime
ano = int(input('quando vcoê nasceu :'))

atual = datetime.date.today().year
idade = atual - ano

if idade <= 10:
    print(f'você tem {idade}anos')
    print('loo você é mirim ')
if 10 < idade < 14:
    print(f'voce tem {idade}anos')
    print(f'a sua classificação é junior')
if 20 < idade < 25:
    print(f'sua idade é {idade}')
    print(f'você esta na classificação senior')
else:
    print('voce esta na classificação master')
