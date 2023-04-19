#  Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

valores = []
maior = 0
menor = 0

for cont in range(0,5):
    valores.append(int(input(f"Digite um numero para a posição {cont}: ")))
    if(0 == cont):
        maior = menor = valores[cont]
    else:
        if(valores[cont] > maior):
            maior = valores[cont]
        if(valores[cont]< menor):
            menor = valores[cont]
print(f"Os valores na lista são {valores}")
print(f"O maior numero é {maior} que está nas posições: ",end="")
for posicao,valor in enumerate(valores):
    if(valor == maior):
        print(f"{posicao}...", end="")
print()
print(f"O menor numero é {menor} que está na posições: ",end="")
for posicao,valor in enumerate(valores):
    if(valor == menor):
        print(f"{posicao}...",end="")