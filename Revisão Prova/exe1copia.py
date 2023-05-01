lista = []

for i in range (10):
    num = int(input(f"Digite o numero da posição {i+1}: "))
    lista.append(num)

impar = []
par = []
cont_impar = 0
for num in lista:
    if(num %2 != 0):
        impar.append(num)
        cont_impar+=1
    else:
        par.append(num)
print(par)
print(impar)
percentual = (cont_impar/len(lista))*100
print(percentual)