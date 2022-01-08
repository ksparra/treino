viagem = float(input('quantos quilometros tem sua viagem ? :'))
if viagem <= 200:
    num = viagem * 0.50
    print(f'você esta prestes a começar uma viagem de {viagem}km/h')
    print(f'o preço da passagem vai ser R${num:.2f}')
else:
    num2 = viagem * 0.45
    print(f'voce começara uma viagem de {viagem}')
    print('o preço de sua viagem vai receber uma promoção:')
    print(f'o preço vai ser {num2:.2f}R$')
