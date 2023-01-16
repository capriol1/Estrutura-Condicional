# Estrutura Condicional: Venda de Combustível

litros = float(input('Números de litros vendido: '))
combustivel = input('Qual o tipo de combustível?(A-Álcool/ G-Gasolina) ').capitalize()
if combustivel == 'A':
    preco = litros * 1.9
    print(f'O valor sem o desconto é R${preco:.2f}')
    if litros <= 20:
        pagar = preco * 0.97
        print(f'O valor a ser pago é R${pagar:.2f}, desconto de 3%')
    if litros > 20:
        pagar = preco * 0.95
        print(f'O valor a ser pago é R${pagar:.2f}, desconto de 5%')
if combustivel == 'G':
    preco = litros * 2.5
    print(f'O valor sem desconto é de R${preco:.2f}')
    if litros <= 20:
        valor = preco * 0.96
        print(f'O valor a ser pago é de R${valor:.2f}, desconto de 4%')
    if litros > 20:
        valor = preco * 0.94
        print(f'O valor a ser pago é de R${valor:.2f}, desconto de 6%')
