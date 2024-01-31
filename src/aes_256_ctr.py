from Crypto.Cipher import AES
from base64 import b64encode, b64decode

#TODO: catch errors and exceptions
class AES256CTR:
    def __init__(self, key, decrypt_nonce=None):
        self.__binary_key = key.encode('utf-8')
        if decrypt_nonce == None:
            self.__cipher = AES.new(self.__binary_key, AES.MODE_CTR)
            self.__nonce = self.__cipher.nonce
        else:
            self.__cipher = AES.new(self.__binary_key, AES.MODE_CTR, nonce=decrypt_nonce)

    def encrypt(self, plaintext):
        binary_plaintext = plaintext.encode('utf-8')
        ciphertext = self.__cipher.encrypt(binary_plaintext)
        return b64encode(ciphertext).decode('utf-8')

    def decrypt(self, ciphertext):
        binary_ciphertext = b64decode(ciphertext)
        return self.__cipher.decrypt(binary_ciphertext).decode('utf-8')

    def get_readable_nonce(self):
        return b64encode(self.__nonce).decode('utf-8')

    @staticmethod
    def create_byte_nonce(readable_nonce):
        return b64decode(readable_nonce)
