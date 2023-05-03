# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça: Mostre a quantidade de valores que foram lidos;

# a. Calcule e mostre a soma dos valores;

# b. Calcule e mostre a média dos valores;

# c. Calcule e mostre a quantidade de valores acima da média calculada;

# d. Calcule e mostre a quantidade de valores abaixo de sete.


notas = []
valor = 0

# lê as notas e armazena na lista "notas"
while valor != -1:
    valor = float(input("Digite uma nota (ou -1 para encerrar): "))
    if valor != -1:
        notas.append(valor)

# mostra a quantidade de valores lidos
print("Quantidade de valores lidos:", len(notas))

# calcula e mostra a soma dos valores
soma = sum(notas)
print("Soma dos valores:", soma)

# calcula e mostra a média dos valores
media = soma / len(notas)
print("Média dos valores:", media)

# calcula e mostra a quantidade de valores acima da média
acima_media = sum(1 for nota in notas if nota > media)
print("Quantidade de valores acima da média:", acima_media)

# calcula e mostra a quantidade de valores abaixo de 7
abaixo_sete = sum(1 for nota in notas if nota < 7)
print("Quantidade de valores abaixo de sete:", abaixo_sete)