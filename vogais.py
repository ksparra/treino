palavras = ('aprender', 'gostar', 'caminhar', 'pendurar'
            , 'lapis', 'gostar', 'celular', 'copo')
for c in palavras:
    print(f'\na palavra {c.upper()} tem a vogal ', end='')
    for o in c:
        if o in 'aeiou':
            print(f'[{o.upper()}]', end=' ')