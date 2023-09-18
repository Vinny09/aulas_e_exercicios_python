import os

palavra_secreta = "hamburguer"
armazenar_letras = ""

contador = 0

while True:
    digitar_letra = input('Digite uma letra ou "exit" para sair: ')
    contador += 1
    if digitar_letra == "exit" or digitar_letra == "Exit" or digitar_letra == "EXIT":
        break
    if len(digitar_letra) > 1:
        print("Digite apenas UMA letra para prosseguir.")
    if digitar_letra in palavra_secreta:
        armazenar_letras += digitar_letra   
    palavra_formada = ""  
    for letra in palavra_secreta:
         if letra in armazenar_letras:
            palavra_formada += letra
         else:
            palavra_formada += "*"
    print(palavra_formada)
    if palavra_formada == palavra_secreta:
        os.system("cls")
        print("VOCÊ GANHOU PARABÉNS!")
        print(f"A palavra era: {palavra_secreta}")
        print(f"Tentativas: {contador}")
        armazenar_letras = ""
        contador = 0