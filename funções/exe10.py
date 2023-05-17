def criar_matriz(linha,coluna):
    matriz = []
    for l in range(linha):
        linha = []
        for c in range(coluna):
            n = int(input(f"Digite um numero para a posição da matriz [{l}][{c}]:  "))
            linha.append(n)
        matriz.append(linha)
    return matriz

def maior_menor(matriz,linha,coluna):
    maior = matriz[0][0]
    menor = matriz[0][0]
    for l in range(linha):
        for  c in range(coluna):
            elemento = matriz[l][c]
            if(elemento > maior):
                maior = elemento
            if(elemento < menor):
                menor = elemento
    return maior,menor

def calcular_media(matriz,linha,coluna):
    soma = 0
    total = linha * coluna
    for l in range(linha):
        for c in range(coluna):
            soma+=matriz[l][c]
    media = soma / total
    return media

def main():
    linha = int(input("Digite o numero de linhas: "))
    coluna = int(input("Digite o numero da coluna: "))
    matriz = criar_matriz(linha,coluna)
    maior,menor = maior_menor(matriz,linha,coluna)
    print("O maior elemento é: ", maior)
    print("O menor elemento é", menor)

    media = calcular_media(matriz,linha,coluna)
    print("A media dos elementos da matriz é: ",media)

if __name__ == "__main__":
    main()