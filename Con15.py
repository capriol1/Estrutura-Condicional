# Estrutura Condicional: validação de triangulos

a = int(input('Qual o tamanho do lado A: '))
b = int(input('Qual o tamanho do lado B: '))
c = int(input('Qual o tamanho do lado C: '))

if a+b > c:
    print('É um trinangulo')
else:
    print('NÃO É UM TRIANGULO!!')
if a == b == c:
    print('Triangulo Equilátero')
elif a == b or a == c or b == c:
    print('Triangulo Isósceles')
elif a != b and a != c and b != c:
    print('Triangulo Escalento')