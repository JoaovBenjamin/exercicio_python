# Escreva um programa em Python para ler uma matriz 3X6 de números reais. Em seguida, quando houver números negativos, troque-os pelo número 1. Por fim, mostre a matriz atualizada

matriz = []

for l in range(3):
    linha = []
    for c in range(6):
        num = int(input("Digite um numero: "))
        linha.append(num)
    matriz.append(linha)

for l in range (3):
    for c in range(6):
        if(matriz[l][c] < 0):
            matriz[l][c] = 1

print("Matriz Atualizada")

for l in range(3):
    for c in range(6):
        print(matriz[l][c], end="")
    print()