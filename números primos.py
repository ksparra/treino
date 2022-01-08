num = int(input('digite um número primo :'))
tot = 0
for c in range (1,num + 1):
    if num % c == 0:
        print(f'{num}')
        tot += 1
if tot == 2:
    print(f'o número foi divisivel {tot}')
else:
    print(f'o número não e divisivel ')
