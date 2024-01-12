## Este código foi elaborado como trablaho academico do aluno Antonio Augusto Borges para Bootcamp DIO Santander


import os
import pyaes

# Abrindo um arquivo criptografado
file_name = 'teste.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# Chave de descriptografia
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo descriptografado
os.remove(file_name)

# Restaurar o arquivo criptografado
new_file = 'teste.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()
