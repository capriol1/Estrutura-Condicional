# Estrutura Condicional: Suspeita sobre crime

a = input('Telefonou para a vitima?(Sim/Não) Resp.:').capitalize()
b = input('Esteve no local do crime?(Sim/ Não) Resp.:').capitalize()
c = input('Mora perta da vítima?(Sim/Não) Resp.:').capitalize()
d = input('Devia para a vítima?(Sim/Não) Resp.:').capitalize()
e = input('Já trabalhou com a vítima?(Sim/Não) Resp.:').capitalize()
cont = 0
if a == 'Sim':
    cont += 1
if b == 'Sim':
    cont += 1
if c == 'Sim':
    cont += 1
if d == 'Sim':
    cont += 1
if e == 'Sim':
    cont += 1
    
if cont == 2:
    print('Suspeita')
if cont == 3:
    print('Cúmplice')
if cont == 4:
    print('Cúmplice')
if cont == 5:
    print('Assassino')
if cont == 0 or cont == 1:
    print('Inocente')