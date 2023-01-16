#Estrutura Condicional: Média do aluno

n1 = int(input('Qual sua primeira nota: '))
n2 = int(input('Qual sua segunda nota: '))
m = (n1 + n2) / 2
print(f'Sua média é {m:.2f}')
if m >= 7 or m < 10:
    print('Aprovado')
elif m == 10:
    print('Aprovado com Distinção')
else:
    print('Reprovado')
