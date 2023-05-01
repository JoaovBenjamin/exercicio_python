# Elaborar um programa em Python que efetue o cálculo de uma tabuada de um número qualquer e armazene os resultados em uma lista A para 11 elementos. Apresentar os valores armazenados na lista

# Ler um número da entrada do usuário
numero = int(input("Digite um número para a tabuada: "))

# Inicializar a lista A com 11 elementos
A = [0] * 11

# Calcular a tabuada e armazenar os resultados na lista A
for i in range(11):
    A[i] = numero * i

# Apresentar os valores armazenados na lista A
print("Tabuada do número", numero)
print(A)