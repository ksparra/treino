from math import sin, tan, cos, radians
num = float(input('coloque o ângulo ? '))

seno = sin(radians(num))
tangente = tan(radians(num))
cosseno = cos(radians(num))

print(f'a tangente do ângulo {num} é {tangente:.2f}')
print(f'a cosseno do ângulo {num} é {cosseno:.2f} ')
print(f'a seno do ângulo {num} é {seno:.2f}')
