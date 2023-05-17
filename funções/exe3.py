# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

def contador(i,f,p):
    print(f"Contagem de {i} até o {f} de {p} em {p}")
    cont = i
    if(p < 0):
        p*= -1
    if p == 0:
        p=1
    if(i < f):   
        while cont <=f:
            print(f"{cont}",end=" ")
            cont+=p
        print("Fim")
    else:
        cont = i
        while cont >=f:
            print(f"{cont}", end=" ")
            cont -=p
        print("Fim")

contador(1,10,1)
contador(30,10,5)
print("Agora é a sua vez de fazer sua contagem")
ini = int(input("Digite um inicio: "))
fim = int(input("Digite o final da sua contagem: "))
pas = int(input("Digite o passador da sua contagem: "))

contador(ini,fim,pas)