# Escreva um programa em Python para ler 15 elementos de uma lista A. Construir uma lista B, observando a seguinte lei de formação: “Todo elemento de B deve ser o quadrado do elemento de A correspondente". Apresentar as listas A e B.

a = []

for i in range(15):
    a.append(int(input(f'Digite o valor {i+1}: ')))

b = []
for i in a:
    b.append(i**2)

print(a)
print(b)