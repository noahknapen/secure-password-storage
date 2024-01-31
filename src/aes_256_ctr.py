from Crypto.Cipher import AES
from base64 import b64encode, b64decode

#TODO: catch errors and exceptions
class AES256CTR:
    def __init__(self, key):
        binary_key = key.encode('utf-8')
        self.__encryption_cipher = AES.new(binary_key, AES.MODE_CTR)
        self.__nonce = self.__encryption_cipher.nonce 
        self.__decryption_cipher = AES.new(binary_key, AES.MODE_CTR, nonce=self.__nonce)

    def encrypt(self, plaintext):
        binary_plaintext = plaintext.encode('utf-8')
        ciphertext = self.__encryption_cipher.encrypt(binary_plaintext)
        return b64encode(ciphertext).decode('utf-8')

    def decrypt(self, ciphertext):
        binary_ciphertext = b64decode(ciphertext)
        return self.__decryption_cipher.decrypt(binary_ciphertext)

    def get_readable_nonce(self):
        return b64encode(self.__nonce).decode('utf-8')
