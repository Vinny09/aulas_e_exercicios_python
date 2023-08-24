while True:

    escolha_operacao = input("Digite a operação que deseja realizar: soma, multiplicação, subtração, divisão ou exponenciação: ")
    num_1 = input("Digite o primeiro numero: ")
    num_2 = input("Digite o segundo numero: ")

    num_1_number = float(num_1)
    num_2_number = float(num_2)
    x = num_1_number
    y = num_2_number

    def function_soma(x, y):
        somar = x + y
        soma_total = f'{somar:.0f}'
        return soma_total

    def function_multiplicacao(x, y):
        multiplicacao = x * y
        multiplicacao_final = f'{multiplicacao:.0f}'
        return multiplicacao_final
    
    def function_subtracao(x, y):
        subtracao = x - y
        subtracao_final = f'{subtracao:.0f}'
        return subtracao_final
    
    def function_divisao(x, y):
        divisao = x / y
        divisao_final = f'{divisao:.2f}'
        return divisao_final
    
    def function_exponenciacao(x, y):
        exponenciacao = x ** y
        exponenciacao_final = f'{exponenciacao:.0f}'
        return exponenciacao_final
    
    if escolha_operacao == 'soma' or escolha_operacao == '+':
        print(f'O Valor da soma de {x} + {y} é igual a = {function_soma(x, y)}')

    elif escolha_operacao == 'multiplicacao' or escolha_operacao == 'x':
        print(f'O Valor da multiplicação entre {x} x {y} é igual a = {function_multiplicacao(x, y)}')

    elif escolha_operacao == 'subtracao' or escolha_operacao == '-':
        print(f'O Valor da subtração entre {x} - {y} é igual a = {function_subtracao(x, y)}')
    
    elif escolha_operacao == 'divisao' or escolha_operacao == '/':
        print(f'O Valor da divisão entre {x} / {y} é igual a = {function_divisao(x, y)}')
    
    elif escolha_operacao == 'exponenciacao' or escolha_operacao == '**':
        print(f'O Valor da exponenciação entre {x} ** {y} é igual a = {function_exponenciacao(x, y)}')

    sair = input("Deseja sair? [s]im ou [c]ontinuar? ")

    if sair == 'sair' or sair == 's' or sair == 'sim':
        break
    else:
        continue
