#Estrutura Condicional: leia 3 numeros e mostre em ordem decresente

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3= int(input('Digite um número: '))
if n3 > n2:
    aux = n3
    n3 = n2
    n2 = aux
if n2 > n1:
    aux = n2
    n2 = n1
    n1 = aux
if n3 > n2:
    aux = n3
    n3 = n2
    n2 = aux

print(n1, n2, n3)