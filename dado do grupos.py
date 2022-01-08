false = False

total18 = 0
homens = 0
mulheres = 0

while not false == True:

    print('-' * 20)
    print('Cadestre uma pessoa')
    print('-' * 20)

    idade = int(input('idade :'))
    sexo = str(input('sexo [F/M] :'))

    print('-' * 20)
    sn = str(input('Quer continuar? [S/N]'))
    print('-' * 20)

    if idade > 18:
        homens += 1

    if sexo == 'M' or 'm':
        total18 += 1

    if sexo == 'F' or 'f':
        mulheres += 1

    if sn == 'N' or 'n':
        false = True

print(f'total de pessoas com mais de 18 anos foi {homens}')
print(f'ao todo temos 1 homen cadastradas ')
print(f'e temos {mulheres} mulheres com menos de 20 ')
