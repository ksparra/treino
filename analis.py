nome = input('Digite seu nome completo:').strip()
print('analisando seu nome')
len(nome)
u = nome.upper()
l = nome.lower()
n = len(nome) - nome.count(' ')
p = nome.split()
print(f'seu nome em maiscula é ={u}')
print(f'seu nome em minuscula é ={l}')
print(f'seu nome tem {n} letras')
print(f'seu primeiro nome é {p[0]} e ele tem {len(p[0])} letras')