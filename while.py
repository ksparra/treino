sexo = str(input('coloque seu genero [F/M]:')).strip().upper()[0]
while sexo not in 'MmfF':
    sexo = str(input('sexo inválido porfavor coloque o certo :')).strip().upper()[0]
if sexo == 'Mm' or 'Ff':
    print(f'o seu genero foi registrado {sexo}')
