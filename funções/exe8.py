def criar_matriz(lin,col):
    matriz = []
    for l in range(lin):
        linha = []
        for c in range(col):
            n = int(input(f"Digite um valor para a posição [{l}][{c}]: "))
            linha.append(n)
        matriz.append(linha)
    return matriz

def exibirMaatriz(matriz):
    print("Matriz: ")
    for linha in matriz:
        print(linha)

def somar_impar(matriz,col):
    soma = 0
    for i in range(len(matriz)):
        if i %2 !=0:
            soma+=matriz[i][col]
    return soma

lin = int(input("Digite o numero de linhas na matriz: "))
col = int(input("Digite o numeros de coluna para a matriz: "))

matriz = criar_matriz(lin,col)
exibirMaatriz(matriz)

coluna_soma = int(input("Digite o número da coluna para somar os índices ímpares: "))

# Calcular a soma dos índices ímpares da coluna especificada
soma_indices_impares = somar_impar(matriz, coluna_soma)

# Exibir o resultado
print("A soma dos índices ímpares da coluna", coluna_soma, "é:", soma_indices_impares)
