# Estrutura Condicional: Frutaria

fruta = input('Qual fruta comprou? (A-Morango/ B-Maça) ').capitalize()
kg = float(input('Quantos Kg: '))
if fruta == 'A':
    if kg <= 5:
        preco = kg * 2.5
        print(f'O valor a ser pago é de R${preco:.2f}')
    elif kg > 5:
        preco = kg * 2.2
        print(f'O valor a ser pago é de R${preco:.2f}')
        if kg >= 8:
            desc = preco * 0.90
            print(f'O valor a ser pago é de R${desc:.2f}, com desconto de 10%')
if fruta == 'B':
    if kg <= 5:
        preco = kg * 1.8
        print(f'O valor a ser pago é de R${preco:.2f}')
    elif kg > 5:
        preco = kg * 1.5
        print(f'O valor a ser pago é de {preco}')
        if kg >= 8:
            desc = preco * 0.90
            print(f'O valor a ser pago é de R${desc:.2f}, com desconto de 10%')
