soma = 0
cont = 0
for i in range (0,502,2):
    if i % 3 == 0:
        soma = soma + i
        cont = cont + 1
print(f'a soma dos valores são {cont} e a soma é {soma}')