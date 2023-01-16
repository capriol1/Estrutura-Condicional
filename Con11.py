# Estrutura Condicional: Organização tabajara, aumento de salario

sal = float(input('Digite seu salário: R$'))
if sal <= 280:
    aum = sal * 0.20
    print(f'Salário antes do reajuste R${sal}\n'
          f'O percentual é de 20%\n'
          f'O aumento é de R${aum:.2f}\n'
          f'O novo salário é de R${sal+aum:.2f}')
elif 280 < sal <= 700:
    aum = sal * 0.15
    print(f'Salário antes do reajuste R${sal}\n'
          f'O percentual de aumento é de 15%\n'
          f'O aumento é de R${aum:.2f}\n'
          f'O novo salário é de R${sal + aum:.2f}')
elif 700 < sal < 1500:
    aum = sal * 0.10
    print(f'Salário antes do reajuste R${sal}\n'
          f'O aumento é de 10%\n '
          f'O aumento é de R${aum:.2f}\n'
          f'O novo salário é de R${sal+aum:.2f}')
elif 1500 <= sal:
    aum = sal * 0.05
    print(f'Salário antes do reajuste R${sal}\n'
          f'O aumento é de 5%\n'
          f'O aumento é de R${aum:.2f}\n'
          f'O nono salário é de R${sal+aum:.2f}')

