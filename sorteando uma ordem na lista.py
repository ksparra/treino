from random import shuffle
a1 = str (input('primeiro: '))
a2 = str (input('segundo: '))
a3 = str (input('terceiro: '))
b1 = str (input(' primeiro: 2b: '))
b2 = str (input(' segundo: 2b: '))
b3 = str (input(' terceiro: 2b: '))

grupo = [a1,a2,a3,]
grupo2 = [b1,b2,b3,]
shuffle(grupo),shuffle(grupo2)
''
print(f'a ordem do primeiro grupo será {grupo}')

print(f'a ordem do segundo grupo será {grupo2}')