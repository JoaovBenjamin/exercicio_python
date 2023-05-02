# Elaborar um programa em Python que efetue o cálculo de uma tabuada de um número qualquer e armazene os resultados em uma lista A para 11 elementos. Apresentar os valores armazenados na lista

num = int(input("Digite um valor para tabuada: "))

a = [num*i for i in range(11)]

print("Tabuada com o numero: ", num)
print(a)