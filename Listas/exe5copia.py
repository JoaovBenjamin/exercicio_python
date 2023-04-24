 #Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valor = []
resp = 0

while(resp == 0):
    valor.append(int(input("Digite os numeros: ")))
    resp = int(input("Se quiser continuar digite 0, caso não digite 1: "))
print(f"A quantidade de numeros digitados foram: {len(valor)}")
valor.sort(reverse=True)
print(valor)
if( 5 in valor):
    print("O numero 5 está na lista")
else: 
    print("O numero 5 não está na lista")