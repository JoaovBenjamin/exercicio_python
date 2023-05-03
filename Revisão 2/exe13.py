# Desenvolva um programa que preencha um vetor com as idades dos usuários até que o usuário digite um valor negativo, o valor negativo não deve ser inserido na lista. Ao final, exiba na tela:

# - A quantidade de usuários menores de 18 anos;

# - A média das idades.

idades = []
idade = 0

while (idade >=0):
    idade = int(input("Digite a idade(caso queira encerrar digite um numero negativo): "))
    idades.append(idade)
idades.pop()

menores = 0
soma_idades = 0

for idade in idades: 
    soma_idades += idade
    if(idade<= 17):
        menores+=1

media = soma_idades/len(idades)


print(idades)
print(f"Quantidade de usuários menores de 18 anos: {menores}")
print(f"Média das idades: {media:.2f}")

