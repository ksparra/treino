print('='*100)
print('LISTA DE PREÇOS ')
print('='*100)

num1 = ('lápis', 1.75,
        'Borracha', 2.5,
        'Estojo', 3.0,
        'pc', 1.000,
        'teclado', 220,
        'caneca', 100)

for p in range(0,len(num1)):
        if p % 2 == 0:
                print(f'{num1[p]:.<30}',end='')
        else:
                print(f'R${num1[p]:>4}')
print('='*50)
