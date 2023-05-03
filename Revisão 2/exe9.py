vogais = input("Digite uma frase: ")

v = "aeiou"

cont = 0

for char in vogais:
    if char in v:
        cont+=1

print(cont)