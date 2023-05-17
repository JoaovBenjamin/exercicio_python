# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(b,h):
    a = b * h
    print(f"O valor da sua area é {a}")
    
    
c = int(input("Digite o valor do comprimento: "))
a = int(input("Digite a altura do terreno: "))
area(a,c)


