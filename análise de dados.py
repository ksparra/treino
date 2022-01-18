num1 = (int(input('Digite um número ')),
        int(input('digite um número ')),
        int(input('digite um número ')),
        int(input('digite um número ')))
print(f'voce digitou os valores {num1}')
print(f'voce digitou o valor 9 {num1.count(9)}vezes')
if 3 in num1:
        print(f'o valor 3 apareceu na {num1.index(3)+1} posição')
else:
        print('o valor tres não foi encontrado')

print(f'os valores pares digitados foi ', end=' ')
for n in num1:
        if n % 2 == 0:
                print(n, end=' ')
