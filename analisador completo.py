media = 0
menor = 0
maior = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 6):
    print(f'-----{p} pessoa ------')
    nome = str(input('nome : '))
    idade = float(input('idade :'))
    sexo = str(input('sexo [F/M] :'))
    media += idade

    if p == 1 and sexo in 'Mn':
        maior = idade
        nomevelho = nome

    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomevelho = nome

    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1


mediaidade = media / 5
print(f'a maior idade entre os homens é {maior}')
print(f'a media de idade entre os 5 é {mediaidade}')
print(f'ao todo tem {totmulher20} com 20 anos a cima ')
