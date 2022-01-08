primeiro = int(input('primeeiro valor :'))
segundo = int(input('segundo valor :'))
sair = False
tot = 1
while not sair:
    print('[1] a soma ')
    print('[2] multiplicador')
    print('[3] maior')
    print('[4] novos números ')
    print('[5] sair ')
    jogador = int(input('escolha a opção:'))

    if jogador == 1:
        print(primeiro + segundo)

    if jogador == 2:
        print(primeiro * segundo)

    if jogador == 3:
        if primeiro>segundo:
            print(f'o maior é {primeiro}')
        if segundo > primeiro:
            print(f'o maior é {segundo}')

    if jogador == 4:
        junto = primeiro+segundo
        amais = int(input('coloque um número a mais:'))
        tot += junto
        print(f'os novos números juntos são :{junto+amais}')

    if jogador >5:
        print('número invalido ')

    if jogador == 5:
        sair = True

print('obrigado por usar')