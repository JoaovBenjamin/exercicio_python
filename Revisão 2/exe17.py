lista1 = []
lista2 = []

for i in range(10):
    num1 = int(input("Digite um número para a lista 1: "))
    lista1.append(num1)
    num2 = int(input("Digite um número para a lista 2: "))
    lista2.append(num2)

lista3 = []

for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(lista1)
print(lista2)
print(lista3)