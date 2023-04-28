# #Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temp = []
princ = []
resp = 0
mai = 0
men = 0

while(resp == 0):
    temp.append(str(input("Digite um nome: ")))
    temp.append(int(input("Digite o peso: ")))
    if(len(princ) == 0):
        mai = temp[1]
        men = temp[1]
    else:
        if(temp[1] > mai):
            mai = temp[1]
        if(temp[1] < men):
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = (int(input("Quer continuar digite 0, caso não digite 1: ")))
print(f'A quantidade de cadastro é {len(princ)}')    
print(f"O menor peso é: {men} ", end="")
for p in princ:
    if(p[1] == men):
        print(f"{p[0]} ", end="")
print()
print(f"O maior peso foi: {mai} ", end="")
for p in princ:
    if(p[1] == mai):
        print(f"{p[0]} ", end="")
print()