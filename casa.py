valor = int(input('qual o valor da casa ? :')) ##o valor da casa é 800 mil
salario = int(input('qual o valor do seu sálario ?:'))  ##o valor do sálario é 10,000
anos = int(input('em quantos anos você planeja pagar a sua casa ? :')) ## 5 anos

mensalidade = valor // (anos *12)
emprestimo = salario * 30 // 100

if emprestimo >= mensalidade :
    print('o emprestimo pode ser feito !!!')
    print(f'o preço da mensalidade é {mensalidade}')
elif emprestimo <= mensalidade:
    print('esse emprestimo não pode ser feito passou de 30 %')
else:
    print('você não tem dinheiro o suficiente')