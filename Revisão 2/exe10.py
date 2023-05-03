# Um palíndromo é um tipo de palavra ou frase que tem a propriedade de ser lida tanto da direita para a esquerda quanto da esquerda para a direita. Como exemplo, temos a palavra “asa”. Baseado nesse conceito, escreva um programa em Python que, dada uma palavra, verifique se ele é um palíndromo ou não. DICA: utiliza a notação de slice.

# Lendo a palavra digitada pelo usuário
palavra = input("Digite uma palavra: ")

# Verificando se a palavra é um palíndromo
if palavra == palavra[::-1]:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
