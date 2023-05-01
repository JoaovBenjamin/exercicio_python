# Escreva um programa em Python para ler uma lista A com 10 elementos numéricos inteiros. Apresentar o total de elementos ímpares existentes na lista e o percentual do valor total de números ímpares em relação à quantidade total de elementos armazenados na lista.

lista = []
par = []
impar = []
cont_impar = 0

for cont in range(1,11):
    valor = int(input(f"Digite o numero {cont}: "))
    lista.append(valor)
    if(valor  %2 == 1):
        impar.append(valor)
        cont_impar+=1
    else:
        par.append(valor)
    prc_impar = (cont_impar/len(lista))*100
print(par)
print(impar)
print(prc_impar)
