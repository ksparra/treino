n = int(input('quantos termos mostrar :'))
m = 1
afrente = 1
passado = 1
num1 = afrente + passado

while m < n:
    m += 1
    num1 += 10
    if num1 > afrente and passado:
        passado += afrente
        afrente += passado
        print(f'{passado} -> {afrente} ->', end=' ')
