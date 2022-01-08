dia = int(input('quantos dias você ficou com o carro ? :'))
km = float(input('quantos km você andou com o carro ? :'))

d = 60
k = 0.15

diaf = dia * d
kmf = km * k

final = diaf + kmf

print(f'você ficou {dia} dias e andou {km} km com o carro entâo pagou {final:.2f}R$')