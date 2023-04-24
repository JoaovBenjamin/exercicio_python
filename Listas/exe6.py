# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
impar = []
par = []
resp = 0

while(resp == 0):
    lista.append(int(input("Digite um numero: ")))
    resp = int(input("Quer continuar digite 0, caso não digite 1: "))

for i,v in enumerate(lista):
    if(v  %2 == 0):
        par.append(v)
    else:
        impar.append(v)

print(lista)
print(par)
print(impar)