from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import json
import os

from aes_256_ctr import AES256CTR
from sha_256 import SHA256
from password_file_operator import PasswordFileOperator

def main():
    origin = input("Enter password origin: ")
    username = input("Enter username used in origin: ")
    data = input("Enter password: ")
    key = input("Enter key: ")

    hash_algorithm = SHA256()
    hashed_key = hash_algorithm.get_hex_hash(key)

    cipher = AES256CTR(hashed_key[0:32])
    nonce = cipher.get_readable_nonce()
    ciphertext = cipher.encrypt(data)

    pw_operator = PasswordFileOperator("../local/encrypted_passwords.json")
    pw_operator.new_origin_entry(origin, username, nonce, ciphertext)

        
if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    main()