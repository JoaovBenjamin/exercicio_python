# Construa um programa em Python para preencher uma matriz, de 6 linhas por 6 colunas, com elementos do tipo int. Em seguida, o programa deve apresentar, na tela, todos os elementos pares contidos na matriz, bem como a posição em que eles se encontram.

matriz = []

for l in range(6):
    linha = []
    for c in range(6):
        num = int(input(f"Digite um numero para o posição da matriz {l}{c}: "))
        linha.append(num)
    matriz.append(linha)

par = []
for l in range(6):
    for c in range(6):
        if(matriz[l][c] %2 == 0):
            par.append(matriz[l][c])

for l in range(6):
    for c in range(6):
        print(f"{matriz[l][c]}",end="")
    print()

print(f"{par}")