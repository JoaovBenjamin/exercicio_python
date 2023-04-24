# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []

while True:
    lista.append(int(input("Digite um numero: ")))
    resp = str(input("Quer continuar[S/N]: "))
    if(resp in "Nn"):
        break

impar = []
par = []

for i,v in enumerate(lista):
    if(v %2 == 0):
        par.append(v)
    else:
        impar.append(v)

print(lista)
print(par)
print(impar)
