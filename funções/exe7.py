def criarMatriz(num_linha, num_colunas):
    matriz = []
    for l in range(num_linha):
        linha = []
        for c in range(num_colunas):
            valor = int(input(f"Digite um valor para a posição [{l}][{c}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def somar_impar(matriz,c):
    soma = 0
    for l in range(len(matriz)):
        if(l % 2 != 0):
            soma+=matriz[l][c]
    return soma

matriz = criarMatriz(3,3)
som_coluna = int(input("Digite o numero da coluna que deseja somar os impares: "))

som_coluna_impar = somar_impar(matriz,som_coluna)

print("A soma dos índices ímpares da coluna", som_coluna, "é:", som_coluna_impar)