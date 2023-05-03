# Escreva um programa que leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.

matriz = []
cont = 0
for l in range(4):
    linha = []
    for c in range(4):
        num = int(input("Digite um numero: "))
        linha.append(num)
    matriz.append(linha)

for l in range(4):
    for c in range(4):
        if(matriz[l][c] > 10):
            cont+=1

print(cont)