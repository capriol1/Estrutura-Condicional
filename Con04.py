#Estrutura Condicional: vogal ou consoante

letra = input('Digite uma letra: ')
if letra == 'a' or letra == 'o' or letra == 'e' or letra == 'i' or letra == 'u':
    print(f'A letra {letra} é vogal')
else:
    print(f'A letra {letra} é consoante')
