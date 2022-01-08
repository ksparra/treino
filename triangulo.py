print(20*'-'*20)
print('analisador de triangulos ')
print(20*'-'*20)
r1 = float(input('seu primeiro segmento :'))
r2 = float(input('seu segundo segmento :'))
r3 = float(input('terceiro segmento :'))

if r1 < r2 and r2 < r1 + r3 and r3 < r1 + r2:
    print('esse segmento pode se tornar um triangulo ')
else:
    print('esse segmento não pode se tornar um segmento ')
