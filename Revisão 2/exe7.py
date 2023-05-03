# Faça um programa que leia uma matriz 3x3 de inteiros e retorne a linha de maior soma. Imprima na tela a matriz, a linha de maior soma e a soma.

matriz =[[0]*3 for l in range(3)]

for l in range(3):
    for c in range(3):
     matriz[l][c]=int(input("Digite um numero: "))

linha_maior = 0
soma_maior = 0

for l in range(3):
    soma_linha = sum(matriz[l])
    if(soma_linha > soma_maior):
        soma_maior = soma_linha
        linha_maior = l+1

print(f"A linha de maior soma é a {linha_maior} com soma {soma_maior}.")
