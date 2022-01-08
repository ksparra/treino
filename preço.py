print('FORMAS DE PAGAMENTO ')
print('A VISTA [1]')
print('A VISTA CARTÃO [2]')
print('2x no cartão [3]')
print('3x ou mais no cartão [4]')
num = int(input('Qual sua opção ?:'))
preco2 = float(input('Preço das compras '))

if num == 1:
    num2 = preco2 - (preco2 * 10 / 100)
    preco = preco2 - num2
    print(f'você comprou a vista logo vai receber um desconto de 10% {preco}R$ :')
    print(f'o preço final é de {num2}')
if num == 2:
    num2 = preco2 - (preco2 * 5 / 100)
    preco = preco2 - num2
    print(f'voce comprou a vista pelo cartão vai receber 5% de desconto {preco}R$2')
    print(f'o preço final é {num2}')
if num == 3:
    parcela = preco2 // 2
    print(f'o preço da compra vai ser {parcela} em 2x ')
if num == 4:
    parcela = int(input('quantas parcelas '))
    parcela2 = preco2 + (preco2 * 20 / 100)
    parcela3 = parcela2 / parcela
    print(f'sua compra de {preco2} vai custar  {parcela2} no final')
    print(f'os juros foram {parcela3:.2f}')

