from math import hypot
c0 = float(input('comprimento do cateto oposto: '))
c1 = float(input('comprimento do cateto adijacent: '))
hi = hypot(c0, c1)
print(f'a hipotenusa é {hi:.2f}')