# Escreva um programa em Python que leia uma matriz M [5x5] e, a cada linha, multiplique cada elemento pelo valor do elemento inserido na diagonal principal da linha. Os elementos da matriz serão fornecidos pelo usuário. Escrever a matriz M lida e a matriz M modificada.


m = [ [0 for c in range(5)] for i in range(5)]

for l in range(5):
    for c in range(5):
        m[l][c] = int(input(f"Digite um numero para a posição {[l]}{[c]}"))

for l in range(5):
    diagonal = m[l][l]
    for c in range(5):
        print(f"{m[l][c]}",end="")
    print()


for l in range(5):
    diagonal = m[l][l]
    for c in range(5):
        m[l][c] *= diagonal

for l in range(5):
    for c in range(5):
        print(f"{m[l][c]}",end="")
    print() 