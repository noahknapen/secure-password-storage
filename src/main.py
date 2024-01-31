from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import json
import os

from aes_256_ctr import AES256CTR
from sha_256 import SHA256
from password_file_operator import PasswordFileOperator

def main():
    operation = input("Do you want to Add or Retrieve a password? [A/R]: ")
    pw_operator = PasswordFileOperator("../local/encrypted_passwords.json")
    origin = input("Enter password origin: ")
    username = input("Enter username used in origin: ")
    key = input("Enter key: ")
    hash_algorithm = SHA256()
    hashed_key = hash_algorithm.get_hex_hash(key)

    if operation == "A":
        data = input("Enter password: ")

        cipher = AES256CTR(hashed_key[0:32])
        nonce = cipher.get_readable_nonce()
        ciphertext = cipher.encrypt(data)

        pw_operator.add_entry(origin, username, nonce, ciphertext)
        print("Password added successfully!")
        return
    elif operation == "R":
        data = pw_operator.retrieve_entry(origin, username)#TODO: check if data is None

        ciphertext = data["ciphertext"]
        nonce = AES256CTR.create_byte_nonce(data["nonce"])
        cipher = AES256CTR(hashed_key[0:32], nonce)
        plaintext = cipher.decrypt(ciphertext)
        print("\nDecrypted password: " + plaintext)
        return
    else:
        print("Invalid operation. Exiting...")
        return

        
if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    main()