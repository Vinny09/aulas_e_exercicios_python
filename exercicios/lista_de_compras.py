lista_de_compras = []

while True:
    print("Selecione uma opção:\n")
    escolha_de_opcao = input("[i]nserir [a]pagar [l]istar: ")
    
    if escolha_de_opcao == "l":
        for index, itens in enumerate(lista_de_compras):
            print(index, itens)

    elif escolha_de_opcao == "i":
        inserir = input("Insira um item na lista: ")
        lista_de_compras.append(inserir)

    elif escolha_de_opcao == "a":
        if not lista_de_compras:
            print("A lista está vazia.")
        else:
            try:
                apagar = int(input("Selecione o indice do item para apaga-lo da lista: "))
                if 0 <= apagar < len(lista_de_compras):
                    lista_de_compras.pop(apagar)
                else:
                    print("Índice do item inexistente.")
            except ValueError:
                print("Por favor, insira um indice valido.")

    else:
        print("Opção invalida, por favor escolha i, a ou l.")
