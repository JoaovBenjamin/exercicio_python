# Escreva um programa em Python para ler 15 elementos de uma lista A. Construir uma lista B, observando a seguinte lei de formação: “Todo elemento de B deve ser o quadrado do elemento de A correspondente". Apresentar as listas A e B.

a = []
b= []

for i in range(15):
    a.append(int(input(f"Digite o valor do {i+1} elemento: ")))

for i in a:
   b.append(i**2)

print("Lista A:", a)
print("Lista B:", b)

