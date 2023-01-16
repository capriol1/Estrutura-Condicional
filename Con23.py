# Estrutura Condicional: se é inteiro ou decinal

num = float(input('Digite qualquer número: '))
if num == round(num):
    print(f'O número {num} é inteiro')
else:
    print(f'O número {num} é decimal')
