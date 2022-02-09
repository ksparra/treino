dados = []
dados.append('pedro')
dados.append('25')
daods2 = dict()
dados2 = {'nome': 'Pedro', 'idade': 25}
print(dados2['nome'])
print(dados2['idade'])
dados2['sexo'] = 'M'
del dados2['sexo']
filme = {'TITULO':'Star wars',
         'ano':1977,
         'dirtetor':'George'}

print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f'o {k} é {v}')
dados.append(filme.copy())