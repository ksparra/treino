lado1 = int(input('o primeiro lado do triangulo :'))
lado2 = int(input('o segundo lado do trianggulo :'))
lado3 = int(input('o terceiro lado do triangulo :'))

if lado2 == lado1 == lado3:
    print('o triangulo é escaleno ')
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado2 or lado3 == lado1 or lado2 == lado1:
    print('o triangulo é isosceles')
else:
    print('o triangulo é escaleno ')
