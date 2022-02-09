nome = str(input('Nome:'))
media = float(input('Media:'))
situacao = ''
if media >= 7:
    situacao = 'Aprovado'
elif 5 <= media < 7:
    situacao = 'media'
else:
    situacao = 'desaprovado'

print('-=-'*10)
conta = {'Nome': f'{nome}', 'Media': f'{media}', 'situação': f'{situacao}'}
for l, k in conta.items():
    print(f'{l} é igual a {k}')


