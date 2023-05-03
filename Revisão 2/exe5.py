# Faça um programa que leia uma matriz 3x3 de inteiros e multiplique os elementos da diagonal principal da matriz por um número k. Imprima a matriz na tela antes e depois da multiplicação.

matriz = []

for l in range(3):
    linha = []
    for c in range(3):
        num = int(input("Digite um elemento: "))
        linha.append(num)
    matriz.append(linha)

print("Matriz Antes de multiplicar: ")
for l in range(3):
    for c in range(3):
        print(matriz[l][c],end="")
    print()

k = int(input("Digite uma constante: "))
for l in range(3):
    matriz[l][l]*=k

print("Matrix depois: ")

for l in range(3):
    for c in range(3):
        print(matriz[l][c],end="")
    print()