# Estrutura Condicional: Media do aluno

n1 = float(input('Qual é sua primeira nota: '))
n2 = float(input('Qual é sua segunda nota: '))
med = (n1 + n2) / 2
if med >= 9 and med <=10:
    print(f'Suas notas são {n1} e {n2}\n'
          f'A média é {med:.2f}\n'
          f'APROVADO com o conceito A')
elif med >= 7.5 and med < 9:
    print(f'Suas notas são {n1} e {n2}\n'
          f'A média é {med:.2f}\n'
          f'APROVADO com o conceito B')
elif med >= 6 and med < 7.5:
    print(f'Suas notas são {n1} e {n2}\n'
          f'A média é {med:.2f}\n'
          f'APROVADO com o conceito C')
elif med >= 4 and med < 6:
    print(f'Suas notas são {n1} e {n2}\n'
          f'A média é {med:.2f}\n'
          f'REPROVADO com o conceito D')
elif med >= 0 and med < 4:
    print(f'Suas notas são {n1} e {n2}\n'
          f'A média é {med:.2f}\n'
          f'REPROVADO com conceito E')
