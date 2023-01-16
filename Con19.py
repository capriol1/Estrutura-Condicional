# Estrutura Condicional: quantidade de centenas, dezenas e unidades

num = int(input('Digite um número: '))
if num < 1000:
    unidade = num % 10
    num = (num - unidade) / 10
    dezena = num % 10
    num = (num - unidade) / 10
    centena = num
dezena = int(dezena)
centena = int(centena)
print(f'{centena} centena(s), {dezena} dezena(s) e {unidade} unidade(s)')