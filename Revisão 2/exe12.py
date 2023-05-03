# Desenvolva um programa que receba 10 números inteiros e os armazene em uma lista. Em seguida, o programa deve encontrar o maior elemento e exibir sua posição (índice) na lista.

lista = []

for i in range(10):
    lista.append(int(input(f"Digite um numero para a posição {i+1}: ")))

maior = lista[0]
posicao = 0

for i in range(i,len(lista)):
    if(lista[i] > maior):
        maior = lista[i]
        posicao = i

print(f"O maior número é {maior} e sua posição na lista é {posicao}.")
