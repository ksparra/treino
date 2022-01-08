from random import shuffle

n1 = str(input('primeiro do grupo: '))
n2 = str(input('segundo do grupo: '))
n3 = str(input('terceiro do grupo: '))

lista = [n1, n2, n3]
shuffle(lista)

print(f'os escolhidos foram')
print(lista)
