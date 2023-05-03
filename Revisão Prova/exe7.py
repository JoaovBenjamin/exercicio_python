# Escreva um programa em Python que leia uma matriz M [5x5] e, a cada linha, multiplique cada elemento pelo valor do elemento inserido na diagonal principal da linha. Os elementos da matriz serão fornecidos pelo usuário. Escrever a matriz M lida e a matriz M modificada.

matriz = []

for l in range(5):
    linha = []
    for c in range(5):
        num = int(input("Digite um numero: "))
        linha.append(num)
    matriz.append(linha)

for l in range(5):
    for c in range(5):
        print(matriz[l][c], end="")
    print()


for l in range(5):
    diagonal = matriz[l][l]
    for c in range(5):
        matriz[l][c]*=diagonal


for l in range(5):
    for c in range(5):
        print(matriz[l][c],end="")
    print()