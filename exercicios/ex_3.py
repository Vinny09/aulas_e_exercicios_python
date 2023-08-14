hora = input("Digite seu horario local: ")

try:
    hora_inteiro = int(hora)
    if hora_inteiro >= 0 and hora_inteiro <= 11:
        print("Bom dia!")
    if hora_inteiro >= 12 and hora_inteiro <= 17:
        print("Boa tarde!")
    if hora_inteiro >= 18 and hora_inteiro <= 23:
        print("Boa noite!")
except Exception as e:
    print("Não foi digitado um horario valido em numero inteiro ou foi digitado numeros floats e palavras.", e)