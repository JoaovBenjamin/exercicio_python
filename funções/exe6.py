def criarLista():
    lista = []
    n = int(input("Digite a quantidade de numeros na sua lista:"))
    for valor in range(n):
        elemento = int(input("Digite o numero para sua lista: "))
        lista.append(elemento)
    return lista

res = criarLista()
print(res)


