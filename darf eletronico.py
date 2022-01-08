carro = float(input('quantos km por hora você estava correndo:'))

if carro >= 80:
    num = carro - 80
    num2 = num*7
    print('multado o valor maximo é 80km/h ')
    print(f'você deve pagar por uma multa de {num2} ')
    multa = str(input('você pagou a multa? :'))
    letra = multa.title()
    final = letra.strip()
    if final == 'Sim':
        print('tudo bem pode ir')
    else:
        print('porfavor pague ou será presso!!!')
else:
    print('tenha um bom dia e dirija bem ')
