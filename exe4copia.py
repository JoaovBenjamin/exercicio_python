# Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = 0
scol = 0
mai = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = (int(input(f"Digite um valor para a {[l]}{[c]}: ")))
for l in range(0,3):
    for c in range(0,3):
        print(f"{matriz[l][c]:>5}",end="")
        if(matriz[l][c] %2 == 0):
            spar += matriz[l][c]   
    print()
print(spar)
for l in range(0,3):
    scol += matriz[l][2]
print(scol)
for c in range(0,3):
    if(c == 0):
        mai = matriz[1][c]
    elif(matriz[1][c] > mai):
        mai = matriz[1][c]
print(mai)

