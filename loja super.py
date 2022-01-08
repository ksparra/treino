print('-' * 20)
print('Loja Super')
print('-' * 20)

total = 0
promaior = 0
barato = 0
obj = 0
produto = ''
probarato = ''


while True:

    produto = str(input('o nome do produto :')).lower().title()
    Preco = int(input('Preço: R$'))
    if obj == 0:
        probarato = produto
        barato = Preco
        obj = obj + 1
    if Preco > 0:
        total = total + Preco
    if Preco > 1000:
        promaior = promaior + 1
    if Preco < barato:
        probarato = produto
        barato = Preco

    res = str(input('Quer continuar ? [S/N] :')).strip().upper()[0]
    if res == 'N':
        break

print('fim do programa')
print(f'o total da compra foi {total}')
print(f'temos {promaior} produto custando mais de R$1000')
print(f'o produto mais barato foi {probarato} que custa {barato}')
