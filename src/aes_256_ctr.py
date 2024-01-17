from Crypto.Cipher import AES
from base64 import b64encode, b64decode


class AES256CTR:
    def __init__(self, key):
        binary_key = key.encode('utf-8')
        self.encryption_cipher = AES.new(binary_key, AES.MODE_CTR) #! Key should be reset before counter resets
        self.nonce = self.encryption_cipher.nonce
        self.decryption_cipher = AES.new(binary_key, AES.MODE_CTR, nonce=self.nonce)
        self.nonce = b64encode(self.encryption_cipher.nonce).decode('utf-8') #? Is nonce necessary to store?

    def encrypt(self, plaintext):
        binary_plaintext = plaintext.encode('utf-8')
        print(binary_plaintext)
        ciphertext = self.encryption_cipher.encrypt(binary_plaintext)
        return b64encode(ciphertext).decode('utf-8')

    def decrypt(self, ciphertext):
        binary_ciphertext = b64decode(ciphertext)
        return self.decryption_cipher.decrypt(binary_ciphertext)

    def get_nonce(self):
        return self.nonce

    def get_key(self):
        return self.key