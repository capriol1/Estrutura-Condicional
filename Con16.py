# Estrutura Condicional: Raízes de uma equação de segundo grau
import math
print('EQUAÇÃO DO SEGUNDO GRAU (ax2 + bx +c) ')
a = int(input('Digite o valor para A: '))
if a == 0:
    print('Valor inválido! Não é uma equação do segundo grau')
else:
    b = int(input('Digite o valor para B: '))
    c = int(input('Digite o valor para C: '))
    delta = b**2 - (4*a*c)
if delta < 0:
    print('A equação não possui raizes reias')
elif delta == 0:
    raiz = -b / (2 * a)
    print(f'Delta igual a 0, possui apenas uma raíz que é {raiz}')
elif delta > 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f'A equação possui duas raízes que são {raiz1} e {raiz2}')
