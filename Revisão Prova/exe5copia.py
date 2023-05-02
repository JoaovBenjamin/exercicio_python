# Escreva um programa em Python para ler 12 elementos inteiros para uma lista A. Construir uma lista B de mesmo tipo e dimensão, observando a seguinte lei de formação: "Todo elemento da lista A que for ímpar deve ser multiplicado por 2; caso contrário, o elemento da lista A deve permanecer constante". Apresentar a lista B

a = []
for i in range(12):
    a.append(int(input("Digite um numero: ")))

b = []

for i in range(12):
    if(a[i] %2 != 0):
        b.append(a[i] * 2)
    else:
        b.append(a[i])

print(a)
print(b)