# Escreva um programa para ler uma matriz A com 8 linhas e 6 colunas. Construir uma lista B que seja formado pela soma de cada linha da matriz A. Ao final apresentar o somatório dos elementos da lista

matriz = [[0]*6 for l in range(8)]

for l in range(8):
    for c in range(6):
        matriz[l][c] = int(input(f"Digite um valor para a posição [{l}] [{c}]: "))
    
lista_b = []
for l in matriz:
    soma_linha = sum(matriz)
    lista_b.append(soma_linha)

soma_linhab = sum(lista_b)
print(soma_linhab)