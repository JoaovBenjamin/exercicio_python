# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior(*num):
    cont = maior = 0
    print("Analisando os numeros ")
    for valor in num:
        print(f"{valor}",end='')   
    print()
    for valor in num:
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont+=1
    print(f"Os valores totais contidos em contador é {cont}")
    print(f"O maior valor é : {maior}")



maior(2,3,4,5,6)
maior(2,4,5,6,7,8)
maior(5,7,8,9)