from math import radians, cos,sin,tan
an = float(input('coloque o angúlo:'))
seno= sin(radians(an))
print(f'o ângulo de {an} tem o seno de :{seno:.2f}')
coss= cos(radians(an))
print(f'o ângulo de {an} tem o cosseno de :{coss:.2f}')
tang= tan(radians(an))
print(f'o ângulo de {an} tem a tangente de :{tang:.2f}')