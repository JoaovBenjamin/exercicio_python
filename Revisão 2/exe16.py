# Faça um programa em Python que leia 10 números inteiros e armazene-os em uma lista. Em seguida, armazene os números pares na lista PAR e os números ÍMPARES na lista ímpar. Por fim, imprima as 3 listas.

# cria as listas vazias
numeros = []
par = []
impar = []

# lê os 10 números
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)
    
    # separa os números pares e ímpares
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

# imprime as listas
print("Números: ", numeros)
print("Pares: ", par)
print("Ímpares: ", impar)
