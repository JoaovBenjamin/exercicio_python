# Faça um programa em Python que peça as 3 notas de 10 alunos, calcule e armazene em uma lista a média de cada aluno. Em seguida, imprima o número de alunos com média maior ou igual a 7.0.

medias = []

for l in range(10):
    notas = []
    for c in range(3):
        nota = float(input(f"Digite a nota {c+1} do aluno {l+1}: "))
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    medias.append(media)

cont = 0

for media in medias:
    if(media >= 7.00):
        cont+=1

print(cont)
