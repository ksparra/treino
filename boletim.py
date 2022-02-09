lista = []
while True:
    nome = str(input('Nome:'))
    nota1 = int(input('Nota 1:'))
    nota2 = int(input('Nota 2:'))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])

    sn = str(input('Quer continuar [S/N]:')).upper()
    if sn not in 'SN':
        print('Invalido')
        break
    if 'N' in sn:
        break

print('==='*10)
print('No.NOme           Media ')
print('==='*10)
for l, b in enumerate(lista):
    print(f'{l:<4}{b[0]:<10}{b[2]:>8.1f}')
