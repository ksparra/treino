digitos = int(input('coloque seu número '))
print(f'analisando seu numero {digitos}')
num = digitos // 1 % 10
num2 = digitos // 10 % 10
num3 = digitos // 100 % 10
num4 = digitos // 1000 % 10
print(f'unidade {num}')
print(f'decimal {num2}')
print(f'centena {num3}')
print(f'milenio {num4}')

