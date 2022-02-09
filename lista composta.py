nome1 = list()
pilha = list()
pesom = 0
pesome = 0
tot = 0

while True:
    nome1.append(str(input('Nome:')))
    nome1.append(int(input('Peso:')))
    if len(pilha) == 0:
        pesom = pesome = nome1[1]
    else:

        if nome1[1] < pesome:

            pesome = len(nome1[1])

        if nome1[1] > pesom:

            pesom = nome1[1]

    pilha.append(nome1[:])
    nome1.clear()

    sn = str(input('voce deseja continuar [s/n]')).upper()

    if sn not in 'SN':
        print('invalido')
        break
    if 'N' in sn:
        break

print('-=-'*5)
print(f'ao todo {len(pilha)} pessoas')
print(f'o maior peso é {pesom} Peso de ', end='')
for p in pilha:
    if p[1] == pesom:
        print(f'{p[0]} ', )

print(f'o menor peso é {pesome} ',end='')
for p in pilha:
    if p[1] == pesome:
        print(f'{p[0]}')
