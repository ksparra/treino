
cont = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez'
        'onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')

while True:
    num1 = int(input('digite um número de 0 até 20:'))

    if num1 > 20:
        num1 = int(input('você digito um número invalido tente novamente :'))
        if num1 > 20:
            print('desisto ')
            break
    break
print(f'voce digitou o número {cont[num1-1]}')






