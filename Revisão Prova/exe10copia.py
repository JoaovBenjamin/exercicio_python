# Faça um programa em Python que conte o número de 1’s que aparecem em uma string. Exemplo: “0011001” = 3.

frase = input("Digite um frase: ")
cont = 0

for car in frase:
    if car == "1":
        cont+=1

print(cont)