def criarMatriz(linha,coluna):
    matriz = []
    for l in range(linha):
        linha = []
        for c in range(coluna):
            n = int(input(f"Digite o valor da matriz na posição [{l}][{c}]"))
            linha.append(n)
        matriz.append(linha)
    return matriz

def exibirMatriz(matriz):
    for l in matriz:
        for i in l:
            print(i, end=" ")
        print()

def diagonalPrincipal(matriz):
    diagonal_principal = []
    for l in range(len(matriz)):
        diagonal_principal.append(matriz[l][l])
    return diagonal_principal

def main():
    linha = int(input("Digite o numero de linhas: "))
    coluna = int(input("Digite o numero de colunas: ")) 

    matriz = criarMatriz(linha,coluna)

    print("Matriz: ")
    exibirMatriz(matriz)

    diagonal = diagonalPrincipal(matriz)
    print("Diagonal Principal: ",diagonal)

if __name__ == "__main__":
    main()   