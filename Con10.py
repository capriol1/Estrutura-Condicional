#Estrutura Condicional: Turno que estuda

turno = input('Qual o turno que você estudo (M-matutino/ V-vesperrino/ N-noturno): ').capitalize()
if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')
