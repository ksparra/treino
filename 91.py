conta = dict()
conta['Nome'] = str(input('Nome:'))
conta['Ano'] = int(input('Ano de nascimento:'))
conta['Carteira'] = int(input('Carteira de trabalho (0 não tem):'))
if conta['Carteira'] > 0:
    conta['Contratação'] = int(input('Ano de contratação:'))
    conta['salario'] = float(input('Salario:'))
    conta['aposentadoria'] = conta['Contratação'] + 35
print(conta)
for k, l in conta.items():
    print(f'{k} tem o valor  {l}')
