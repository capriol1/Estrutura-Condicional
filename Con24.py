# Estrutura Condiciona: e leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realiza

num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
ope = input('Dejesa realizar qual operação(A-Adição/ B-Subtração/ C-Divisão/ D-Mutiplicação): ').capitalize()

if ope == 'A':
    soma = num1 + num2
    print(f'O resultado é {soma:.2f}')
    if soma % 2 == 0:
        print(f'O resultado é par')
    else:
        print(f'O resultado é ímpar')
    if soma >= 0:
        print('O resultado é positivo')
    else:
        print('O resultadoo é negativo')
    if soma == round(soma):
        print('O resultado é interio')
    else:
        print('O resultado é decimal')
elif ope =='B':
    sub = num1 - num2
    print(f'O resultado é {sub:.2f}')
    if sub % 2 == 0:
        print('O resultado é par')
    else:
        print('O resultado é ímpar')
    if sub >= 0:
        print('O resultado é positivo')
    else:
        print('O resultado é negativo')
    if sub == round(sub):
        print('O resultado é inteiro')
    else:
        print('O resultado é decimal')
elif ope == 'C':
    div = num1 / num2
    print(f'O resultado é {div:.2f}')
    if div % 2 == 0:
        print('O resultado é par')
    else:
        print('O resulado é ímpar')
    if div >= 0:
        print('O resultado é positivo')
    else:
        print('O resultado é negativo')
    if div == round(div):
        print('O resultado é inteiro')
    else:
        print('O resultado é decinal')
elif ope == 'D':
    mult = num1 * num2
    print(f'O resuultado é {mult:.2f}')
    if mult % 2 == 0:
        print('O resultado é par')
    else:
        print('O resultado é ímpar')
    if mult >= 0:
        print('O resultado é positivo')
    else:
        print('O resultado é negativo')
    if mult == round(mult):
        print('O resultado é inteiro')
    else:
        print('O resultado é decimal')