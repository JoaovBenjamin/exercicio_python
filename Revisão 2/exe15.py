# Escreva um programa que simule um dicionário inglês/português utilizando o conceito de listas. Para tanto, crie uma lista para as palavras em inglês e outra para as traduções em português nas respectivas posições. A inserção das palavras deverá ser executada até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO). Após a inserção, exiba a tradução em português de uma determinada palavra em inglês que o usuário deverá digitar.

ingles = []

# Lista de traduções em português
portugues = []

# Loop de inserção de palavras
while True:
    # Solicita a palavra em inglês
    palavra = input("Digite uma palavra em inglês (ou 0 para sair): ")
    
    # Verifica se o usuário deseja sair
    if palavra == '0':
        break
    
    # Adiciona a palavra na lista de inglês
    ingles.append(palavra)
    
    # Solicita a tradução em português
    traducao = input("Digite a tradução em português: ")
    
    # Adiciona a tradução na lista de português
    portugues.append(traducao)
    
    # Pula uma linha
    print()

# Solicita uma palavra para tradução
palavra_busca = input("Digite uma palavra em inglês para obter a tradução: ")

# Procura a palavra na lista de inglês
indice = -1
for i in range(len(ingles)):
    if ingles[i] == palavra_busca:
        indice = i
        break

# Exibe a tradução se encontrar a palavra
if indice >= 0:
    print(f"A tradução de {palavra_busca} é {portugues[indice]}.")
else:
    print("Palavra não encontrada.")