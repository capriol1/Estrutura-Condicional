#Estrutura Condicional: Média

n1 = float(input('Digite sua primeira nota parcial: '))
n2 = float(input('Digite sua segunda nota parcial: '))
n3 = float(input('Digite sua terceira nota parcial: '))
media = (n1 + n2 + n3) / 3
if media >= 7:
    print(f'Aprovado com média {media:.2f}')
elif media < 7:
    print(f'Reoprovado com média {media:.2f}')
elif media == 10:
    print(f'Aprovado com Distinção com média {media:.2f}')
