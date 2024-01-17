from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from aes_256_ctr import AES256CTR
from sha_256 import SHA256

def main():
    data = "secret"
    key = "very secure key"
    hash_algorithm = SHA256()
    hashed_key = hash_algorithm.get_hex_hash(key)
    print(hashed_key)
    cipher = AES256CTR(hashed_key[0:32])
    ciphertext = cipher.encrypt(data)
    print(ciphertext)
    plaintext = cipher.decrypt(ciphertext)
    print(plaintext)
    
if __name__ == "__main__":
    main()