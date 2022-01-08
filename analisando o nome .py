nome = str(input('digite seu nome completo :'))

up = nome.upper()

print(f'o seu nome com as letras maisculas : {up}')

down = nome.lower()

print(f'seu nome com as letras minusculas : {down}')

analy = len(nome.strip()) - nome.count(' ')

print(f'quantas letras tem : {analy}')

prime = nome.find(' ')

nomes = nome.split()

print(f'seu primeiro nome é {nomes[0]} e ele tem :{prime} letras')
