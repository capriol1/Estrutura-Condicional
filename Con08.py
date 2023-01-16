#Estrutura Condicional: leia 3 protudos é mostre qual deve comprar

v1 = float(input('Digite o primeiro preço do produto: R$'))
v2 = float(input('Digite o segundo preço do produto: R$'))
v3 = float(input('Digite o terceiro preço do produto: R$'))
if v1 < v2 and v1 < v3:
    print(f'O protudo que deve ser comprado com o menor preço é primeiro com o valor de R${v1}')
if v2 < v1 and v2 < v3:
    print(f'O produto que deve ser comprado com o menor preço é o segundo com o valor de R${v2}')
if v3 < v1 and v3 < v2:
    print(f'O produto que deve ser comprado com o menor preço é o terceiro com o valor de R${v3}')
