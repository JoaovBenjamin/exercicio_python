# Faça um programa que leia uma matriz 6x3 com números reais, calcule e mostre:

# (a) o maior elemento da matriz e sua respectiva posição (linha e coluna); (b) o menor elemento da matriz e sua respectiva posição.

matriz = [[0]*3 for l in range(6)]

for l in range(6):
    for c in range(3):
        matriz[l][c] = int(input("Digite um numero: "))

maior = matriz[0][0]
pos_mai = [0,0]
menor = matriz[0][0]
pes_men = [0,0]

for l in range(6):
    for c in range(3):
        if(matriz[l][c] > maior):
            maior = matriz[l][c]
            pos_mai = [l+1,c+1]
        if(matriz[l][c] < menor):
            menor = matriz[l][c]
            pes_men = [l+1,c+1]

print(f"O maior elemento da matriz é {maior}, na posição {pos_mai}.")
print(f"O menor elemento da matriz é {menor}, na posição {pes_men}.")