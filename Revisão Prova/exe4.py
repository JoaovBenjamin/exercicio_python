# Elaborar um programa em Python que efetue o cálculo de uma tabuada de um número qualquer e armazene os resultados em uma lista A para 11 elementos. Apresentar os valores armazenados na lista

A = [0] * 11 

num = int(input("Digite um numero para tabuada: "))

for i in range(11):
    A[i] = num * i

print("Tabuada do numero", num)
print(A)