frase = str(input('digite uma frase:')).strip().upper()
Anal = frase.split()
junto = ''.join(frase)
inverso = ''
for c in range (len(junto)-1 ,-1,-1,):
    inverso += junto[c]
if inverso == junto:
    print('e um palidramo ')
else:
    print('a frase digitada  nao e um problema')
