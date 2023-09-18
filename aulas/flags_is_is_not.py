"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

"""
Se eu quiser usar uma constante (Variavel que não muda o valor)
só definir toda a variavel com uppercase (LETRAS MAIUSCULAS)
podendo ter qualquer valor.
exemplo abaixo:
VARIAVEL_CONSTANTE = "Essa é uma variavel constante"
VARIAVEL_CONSTANTE_NUMERO = 10
"""

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')