def criar_lista(linha):
    lista = []
    for i in range(linha):
        n = int(input(f"Digite um numero para a posição {i+1}: "))
        lista.append(n)
    return lista

def impar(lista):
    total = 0
    for i in lista:
        if(i %2 != 0):
            total+=1
    percentual = (total/len(lista)) * 100
    return total,percentual

def triplo(lista):
    nova_lista = []
    for i in lista:
        novo = i * 3
        nova_lista.append(novo)
    return nova_lista

def main():
    tam_lista = int(input("Digite o tamanho da sua lista: "))
    lista = criar_lista(tam_lista)
    print("Lista carregada: ", lista)

    total_impar, percentual = impar(lista)
    print("Total de elementos ímpares:", total_impar)
    print("Percentual de elementos ímpares:", percentual, "%")

    lista_tripla = triplo(lista)
    print("A lista com os novos elementos: ", tam_lista)

if __name__ == "__main__":
    main()