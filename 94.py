lista = {}
lista2 = []
tot = 0
soma = 0
tot1 = 0
culher = ''

while True:
    lista['Nome'] = str(input('Nome:'))
    lista['Sexo'] = str(input('Sexo[M/f]:')).upper()

    if lista['Sexo'] not in 'MF':
        print('apenas f ou m ')
        lista['Sexo'] = str(input('Sexo[M/F]:')).upper()

    lista['Idade'] = int(input('Idade:'))
    soma += lista['Idade']
    lista2.append(lista.copy())

    lista['sn'] = str(input('Quer continuar [S/N]')).upper()
    if lista['sn'] not in 'SN':
        print('invalido')
        lista['sn'] = str(input('Quer continuar [S/N]:')).upper()

    tot += 1
    if 'N' not in lista['sn']:
        continue
    break
print('-=-'*5)
print(f'Ao todo temos {tot} pessoas cadastradas')
media = soma / tot
print(f'A media de idade é {media}')
print(f'as mulhers cadastradas foram ',end='')
for p in lista2:
    if lista['Idade'] >= media:
        print('    ')
        for k, v in lista.items():
            print(f'{k} = {v}; ', end='')
            print()
print('ACABO')
