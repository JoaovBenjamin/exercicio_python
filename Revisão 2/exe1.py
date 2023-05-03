# Escreva um programa para ler uma matriz A com 8 linhas e 6 colunas. Construir uma lista B que seja formado pela soma de cada linha da matriz A. Ao final apresentar o somatório dos elementos da lista B

matriz = []
for l in range(8):
    linha = []
    for c in range(6):
        num = int(input(f"Digite um numero para a posição da matriz a [{l}] [{c}]: "))
        linha.append(num)
    matriz.append(linha)

lista_b = []
for l in matriz:
    soma_linha = sum(l)
    lista_b.append(soma_linha)

soma_listab = sum(lista_b)
print(soma_listab)