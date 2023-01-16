#Estrutura Condicional: Impsoto de Renda

gan = float(input('Digite quanto ganha por hora: '))
hora = int(input('Digite quantas hora trabalhadas por mês: '))
sal_bruto = gan * hora
if sal_bruto <= 900:
    fgts = sal_bruto * 0.11
    inss = sal_bruto * 0.10
    print(f'Salário Bruto: ({gan} * {hora}) R${sal_bruto:.2f}\n'
          'Insento de IR\n'
          f'(-) INSS (10%): R${inss:.2f}\n'
          f'FGTS(11%): R${fgts:.2f}\n'
          f'Total de desconto: R${inss:.2f}\n'
          f'Salário Liquido: R${sal_bruto-inss:.2f}')
elif 900 < sal_bruto <= 1500:
    fgts = sal_bruto * 0.11
    inss = sal_bruto * 0.10
    ir = sal_bruto * 0.05
    print(f'Salário Bruto: ({gan} * {hora}) R${sal_bruto:.2f}\n'
          f'(-) IR (5%):  R${ir:.2f}\n'
          f'(-) INSS (10%): R${inss:.2f}\n'
          f'FGTS (11%): R%{fgts:.2f}\n'
          f'Total de desconto: R${ir + inss:.2f}\n'
          f'Salário Liquido: R${sal_bruto - ir - inss:.2f}')
elif 1500 < sal_bruto <= 2500:
    fgts = sal_bruto * 0.11
    inss = sal_bruto * 0.10
    ir = sal_bruto * 0.10
    print(f'Salário Bruto: ({gan} * {hora}) R${sal_bruto:.2f}\n'
          f'(-) IR (10%): R${ir:.2f}\n'
          f'(-) INSS (10%): R${inss:.2f}\n'
          f'FGTS (11%): R${fgts:.2f}\n'
          f'Total de desconto: R${ir + inss:.2f}\n'
          f'Salário Liquido: R${sal_bruto - ir -inss:.2f}')
else:
    fgts = sal_bruto * 0.11
    inss = sal_bruto * 0.10
    ir = sal_bruto * 0.20
    print(f'Salário Bruto: ({gan} * {hora}) R${sal_bruto:.2f}\n'
          f'(-) IR (20%): R${ir:.2f}\n'
          f'(-) INSS (10%): R${inss:.2f}\n'
          f'FGTS (11%): R%{fgts:.2f}\n'
          f'Total de descontos: R${ir + inss:.2f}\n'
          f'Salário Liquido: R${sal_bruto - ir - inss:.2f}')
