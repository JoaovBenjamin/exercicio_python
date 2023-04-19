#  Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

valores = []
maior = 0
menor = 0

for cont in range(0,5):
    valores.append(int(input(f"Digite um numero para posição {cont}: ")))
    if(cont == 0):
        maior = valores[cont]
        menor = valores[cont]
    else:
        if(valores[cont] > maior):
            maior = valores[cont]
        if(valores[cont] < menor):
            menor = valores[cont]
print(f"Os valores digitados foram {valores}")
print(f"O maior numero e {maior} nas posições ", end="")
for posicao,valor in enumerate(valores):
    if(valor == maior):
        print(f"{posicao}...", end="")
print()
print(f"O maior numero e {menor} nas posições ", end="")
for posicao,valor in enumerate(valores):
    if(valor == menor):
        print(f"{posicao}...", end="")





