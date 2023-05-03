# Crie um programa que recebe uma string e um caractere digitado pelo usuário e retorne o número de vezes que esse caractere aparece na string.

string = input("Digite uma frase: ")
carac = input("Digite um caractere: ")
cont = 0
for caract in string:
    if caract == carac :
        cont+=1
print("O caracter", caract, "aparece",cont)