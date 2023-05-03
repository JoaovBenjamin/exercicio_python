matriz = []
cont = 0
for l in range(4):
    linha = []
    for c in range(4):
        num = int(input("Digite um numero: "))
        if(num > 10):
            cont+=1
        linha.append(num)
    matriz.append(linha)

print(cont)