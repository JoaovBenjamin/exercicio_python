def calcular_tabuada(n):
    lista = []
    for i in range(1,11):
        resultado = n * i
        lista.append(resultado)
    return lista

def fatorial(n):
    fatorial = 1
    for i in range(1,n+1):
        fatorial *= i
    return fatorial

def main():
    n = int(input("Digite um numero: "))
    tabuada = calcular_tabuada(n)
    print("Tabuada do",n,": ",tabuada)

    fat = fatorial(n)
    print("Fatorial de", n, ": ", fat)

if __name__ == "__main__":
    main()
