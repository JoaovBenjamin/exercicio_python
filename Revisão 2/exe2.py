# Escreva um programa que leia uma lista A com 10 elementos. Construir uma matriz C com três colunas, em que a primeira coluna da matriz C é formada pelos elementos da lista A somados com mais 5, a segunda coluna é formada pelo triplo de cada elemento correspondente da lista A e a terceira e última coluna deve ser formada pelos quadrados dos elementos correspondentes da lista A. Por fim, mostre os elementos da matriz C

lista = []
for i in range(10):
    lista.append(int(input(f"Digite o {i+1} da lista: ")))

matriz = [[0]*3 for i in range(10)]
for i in range(10):
    matriz[i][0] = lista[i] + 5
    matriz[i][1] = lista[i] * 3
    matriz[i][2] = lista[i] ** 2

for l in range(10):
    for c in range(3):
        print(f"{matriz[l][c]:>5}", end="")
    print()