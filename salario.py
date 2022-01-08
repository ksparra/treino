sal = int(input('qual é o salario do funcionário ? :'))
if sal <= 1500:
   num = sal + (sal * 15 / 100)
   print(f'o seu novo aumeneto é de {num}')
else:
    novo = sal * (sal * 10 / 100)
    print(f'seu novo salario é {novo:.2f}')
