nome = input("Digite seu nome: ")

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice +=1

novo_nome += '*' # Adiciona o * no final do nome digitado
print(novo_nome)