def criar_matriz(linha,coluna):
    matriz = []
    for l in range(linha):
        linha = []
        for c in range(coluna):
            n = int(input(f"Digite o numero para a posição da matriz [{l}][{c}]: "))
            linha.append(n)
        matriz.append(linha)
    return matriz

def impar(matriz):
    soma = 0
    for l in matriz:
        for elemento in l:
            if(elemento %2 !=0):
                soma+=elemento
    return soma

def exibirMatriz(matriz):
    for l in matriz:
        for elemento in l:
            print(elemento, end =" ")
        print()


def main(): 
    linha = int(input("Digite o numero de linhas: "))
    coluna = int(input("Digite o numero de colunas: "))

    matriz= criar_matriz(linha,coluna)

    soma_impar = impar(matriz)

    print("O somatorio dos elementos impares são: ",soma_impar)

    print("Matriz: ")
    exibirMatriz(matriz)

if __name__ == "__main__":
    main()

