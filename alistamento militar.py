from datetime import date
ano = int(input('em qual ano você nasceu :'))

atual = date.today().year

idade = atual - ano

if idade < 18:
    print('você não pode se alistar ainda ')
    print(f'você tem {idade} anos')
elif idade >= 18:
    print('párabens voce ja pode se alistar')
