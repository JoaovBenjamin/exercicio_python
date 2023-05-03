# Crie um programa que recebe uma string e um caractere digitado pelo usuário e retorne o número de vezes que esse caractere aparece na string.

string = input("Digite um frase: ")
c = input("Digite um caractere: ")
cont = 0
for ca in string:
    if(ca == c):
        cont+=1

print(cont)