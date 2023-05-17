# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint

def sorteia(lista):
    for cont in range(0,5):
        n = randint(1,10)
        numeros.append(n)
        print(f"{n} ",end=" ",flush=True)

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor %2 == 0:
            soma+=valor
    print(f"Somando os pares temos o valor: {soma}")
print()

numeros = []
sorteia(numeros)
somaPar(numeros)
