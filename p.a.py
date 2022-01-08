print('*'*10)
print('A SOMA DOS TERMOS DE UMA P.G ')
print('*'*10)

primeiro = int(input('o primeiro termo de uma p.a:'))
razao = int(input('a razão da p.a:'))
decimo = primeiro + (10 - 1) * razao

for p in range (primeiro,decimo,razao):
    print(p)
