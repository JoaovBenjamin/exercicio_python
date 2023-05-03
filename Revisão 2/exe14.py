# Desenvolva um programa que recebe 10 números inteiros e os armazene em uma lista. Em seguida, exiba quantos números múltiplos de 3 ela possui.

lista = []
tres = []

for i in range(10):
  numero = int(input(f'Digite o {i+1}º número inteiro: '))
  lista.append(numero)

cont = 0
for numero in lista:
    if numero %3 == 0:
       cont+=1
      
print(lista)
print(cont)