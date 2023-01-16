# Estruturas Condicionias: Hipermercado

carne = int(input('Qual carne vai comprar?(1-File Duplo/2-Alcatra/3-Picanha) '))
kg = float(input('Quantos quilos: '))
cartao = input('Vai pagar com cartão Tabajara? (Sim/Não) ').capitalize()

if carne == 1:
    print('Carne: File Duplo')
    if kg <= 5:
        preco = kg * 4.9
        print(f'Preço total: R${preco:.2f}')
    elif kg > 5:
        preco = kg * 5.8
        print(f'Preço total: R${preco:.2f}')
    if cartao == 'Sim':
            desc = preco * 0.05
            pagar = preco - desc
            print(f'Desconto de 5%: R${desc:.2f}\n'
                  f'Valor a pagar: R${pagar:.2f}')
if carne == 2:
    print('Carne: Alcatra')
    if kg <= 5:
        preco = kg * 5.9
        print(f'Preço total: R${preco:.2f}')
    elif kg > 5:
        preco = kg * 6.8
        print(f'Preço total: R${preco:.2f}')
    if cartao == 'Sim':
            desc = preco * 0.05
            pagar = preco - desc
            print(f'Desconto de 5%: R${desc:.2f}\n'
                  f'Valor a pagar: R${pagar:.2f}')
if carne == 3:
    print('Carne: Picanha')
    if kg <= 5:
        preco = kg * 6.9
        print(f'Preço total: R${preco:.2f}')
    elif kg > 5:
        preco = kg * 7.8
        print(f'Preço total: R${preco}')
    if cartao == 'Sim':
            desc = preco * 0.05
            pagar = preco - desc
            print(f'Desconto de 5%: R${desc:.2f}\n'
                  f'Valor a pagar: R${pagar:.2f}')