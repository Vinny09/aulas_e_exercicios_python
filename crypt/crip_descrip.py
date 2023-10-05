from cryptography.fernet import Fernet

# Função para gerar a chave e salvar a chave em um arquivo
def generate_key_and_save_to_file(filename):
    # Gerando uma chave
    global key
    key = Fernet.generate_key()

    # Salvando a chave em um arquivo
    with open(filename, 'wb') as filekey:
        filekey.write(key)

# Função para criptografar o arquivo desejado
def encrypt_file(input_filename, output_filename, key):
    # Usando a chave
    fernet = Fernet(key)

    # Abrindo o arquivo original para criptografar
    with open(input_filename, 'rb') as file:
        original = file.read()

    # Criptografar o arquivo
    encrypted = fernet.encrypt(original)

    # Abrir o arquivo de saída no modo de gravação e
    # gravar os dados criptografados
    with open(output_filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# Função para descriptografar um arquivo
def decrypt_file(input_filename, output_filename, key):
    # Usando a chave
    fernet = Fernet(key)

    # Abrindo o arquivo criptografado para descriptografar
    with open(input_filename, 'rb') as enc_file:
        encrypted = enc_file.read()

    # Descriptografando o arquivo
    decrypted = fernet.decrypt(encrypted)

    # Abrindo o arquivo de saída no modo de gravação e
    # gravando os dados descriptografados
    with open(output_filename, 'wb') as dec_file:
        dec_file.write(decrypted)

# Exemplo de uso das funções:

# Gerar uma chave e salvá-la em um arquivo
generate_key_and_save_to_file('filekey.key')

# Criptografar um arquivo
encrypt_file('./test.txt', 'test_encrypted2.txt', key)

# Descriptografar um arquivo
decrypt_file('test_encrypted.txt', 'test_decrypted2.txt', key)
