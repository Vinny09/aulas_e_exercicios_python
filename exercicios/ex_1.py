while True:
    name = input("Digite o seu nome: ")
    age = input("Digite a sua idade: ")

    if name and age:
        print(f"Seu nome é {name} \n Seu nome invertido é {name[::-1]}")

        if " " in name:
            print("Seu nome contém espaços")
        else:
            print("Seu nome não contém espaços")
        
        letter_count = len(name.replace(" ", "")) # Metodo .replace foi adicionado para não contar os espaços do nome 
        print(f"Seu nome contém {letter_count} letras")

        print(f"A primeira letra do seu é {name[0]}")
        print(f"A ultima letra do seu é {name[-1]}")
        break
    else:
        print("Nada foi digitado, tente novamente.")
    

        
    


