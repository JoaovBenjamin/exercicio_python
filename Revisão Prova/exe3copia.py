# Escreva um programa em Python para ler duas listas A e B com 10 elementos cada. Construir uma lista C, sendo esta a junção das 2 outras listas. Desta forma C deve ter o dobro de elementos em relação às listas A e B, ou seja, a lista C deverá possuir 20 elementos. Apresentar a lista C.

a = []
for i in range(10):
    a.append(int(input("Digite o elemento da lista A: ")))

b = []
for i in range(10):
    b.append(int(input("Digite um valor para a lista B: ")))

C = []
C = a+b
print(C)