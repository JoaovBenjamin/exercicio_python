valor = []
while True:
    valor.append(int(input("Digite um numero: ")))
    resp = str(input("Quer continuar S/N: "))
    if(resp in "Nn"):
         break
print(f"Os valores da sua lista são: {len(valor)}")
valor.sort(reverse=True)
print(valor)
if 5 in valor:
     print("O valor 5 esta adicionado")
else:
     print("O valor 5 não está adicionado")