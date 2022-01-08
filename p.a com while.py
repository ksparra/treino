print('gerador de p.a')
print('-'*20)

num1 = int(input('primeiro termo da p.a :'))
num2 = int(input('segundo a razão de uma p.a :'))
resultado = num1 + (num2 * 10)
tot = num1 + (num2 * 10)

while tot > 0:
    tot -= num2
    print(f'{tot}' ' ', end='')
print('fim')

