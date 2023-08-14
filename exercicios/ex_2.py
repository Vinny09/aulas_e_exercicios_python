num = input("Digite um numero inteiro: ")

if num.isdigit():
    num_inteiro = int(num)
    if num_inteiro % 2 == 0:
        print(f"O numero {num_inteiro} é par.")
    else:
        print(f"O numero {num_inteiro} é impar.")
else:
    print("O numero digitado não é um inteiro.")
