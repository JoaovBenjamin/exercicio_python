data_nascimento = input("Digite a data de nascimento no formato dd/mm/aaaa: ")

# Divide a string em dia, mês e ano
dia, mes, ano = data_nascimento.split('/')

# Define uma lista com os nomes dos meses por extenso
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

# Imprime a data com o nome do mês por extenso
print(f'{dia} de {meses[int(mes)-1]} de {ano}')