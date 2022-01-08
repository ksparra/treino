from random import choice

n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))

grupo = [n1, n2, n3]

escolhido = choice(grupo)

print(f'o escolhido do dos três é o :{escolhido}')
