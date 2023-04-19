# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

valores = list()
resp = 0

while(resp == 0 ):
    valor = int(input("Digite um numero: "))
    if valor not in valores:
        valores.append(valor)
        print("Valor adicionado")
    else:
        print("Valor já existe em sua lista, digite outro numero")
    resp = int(input("Quer continuar, digite 0: "))
valores.sort()
print(valores)