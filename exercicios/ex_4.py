nome = input("Digite somente seu primeiro nome: ")

letras_nome = len(nome)

if letras_nome <= 4:
    print("Seu nome é curto.")

if letras_nome == 5 or letras_nome == 6:
    print("Seu nome é normal.")
    
elif letras_nome > 6:
    print("Seu nome é muito grande.")

