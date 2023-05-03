# Elaborar um programa que efetue a leitura de 20 valores inteiros em uma matriz A com 4 linhas e 5 colunas. Construir uma lista B para 4 elementos que seja formada pelo somatório dos elementos correspondentes de cada linha da matriz A. Construir também uma lista C para 5 elementos que seja formada pelo somatório dos elementos correspondentes de cada coluna da matriz A. Ao final o programa deve apresentar os elementos da lista B e da lista C.

matriz = [[0]*5 for l in range(4)]


for l in range(4):
    for c in range(5):
        matriz[l][c] = int(input(f"Digite um valor para a posição [{c}] [{l}]: "))

listab = []

for l in matriz: 
    soma_linha = sum(l)
    listab.append(soma_linha)

listac = []
for c in range(5):
    soma_col = 0
    for l in range(4):
        soma_col += matriz[l][c]
    listac.append(soma_col)


print("Lista A: ")
for l in range(4):
    print(listab,end="")
print()

print("Lista C: ")
for c in range(5):
    print(listac,end="")
print()