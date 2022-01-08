soma = 0
while True:
    num = int(input('digite um valor :'))
    if num == 999:
        break
    soma += num
print(f'a soma dos valores sem o 999 é {soma}')