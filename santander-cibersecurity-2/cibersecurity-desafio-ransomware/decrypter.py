import os
import pyaes

class FileDecrypter:
    def __init__(self, file_name, key):
        self.file_name = file_name
        self.key = key

    def decrypt_file(self):
        with open(self.file_name, "rb") as file:
            file_data = file.read()

        os.remove(self.file_name)

        aes = pyaes.AESModeOfOperationCTR(self.key)
        decrypt_data = aes.decrypt(file_data)

        new_file_name = self.file_name.replace(".ransomwaretroll", "")
        with open(new_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

if __name__ == "__main__":
    key = b"testeransomwares"
    decrypter = FileDecrypter("teste.txt.ransomwaretroll", key)
    decrypter.decrypt_file()