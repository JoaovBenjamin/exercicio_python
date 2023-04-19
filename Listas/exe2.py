# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

valores = list()
while True:
    valor=(int(input("Digite um numero: ")))
    if valor not in valores:
        valores.append(valor)
        print("Valor adicionado")
    else:
        print("Numero já existe em sua lista, digite outro valor")
    resp = str(input("Quer continuar ? [S/N]"))
    if resp in "Nn":
        break
valores.sort()
print(f"A sua lista é: {valores} ")