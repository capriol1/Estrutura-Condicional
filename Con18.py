# Estrutura Condicional: validação de data

print('O formato da data é dd/mm/aaaa')
dd = int(input('Digite o dia: '))
mm = int(input('Digite o mês: '))
aa = int(input('Digite o ano: '))
valida = False
if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
    if dd <= 31:
        valida = True
elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
    if dd <= 30:
        valida = True
elif mm == 2:
    if aa % 4 == 0 and aa % 100 != 0 or aa % 400 == 0:
        if dd <= 29:
            valida = True
        elif dd <= 28:
            valida = True
if valida:
    print('Data válida')
else:
    print('Inválida')
