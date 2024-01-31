from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from aes_256_ctr import AES256CTR
from sha_256 import SHA256
import json
import os

def main():
    origin = input("Enter password origin: ")
    data = input("Enter password: ")
    key = input("Enter key: ")

    hash_algorithm = SHA256()
    hashed_key = hash_algorithm.get_hex_hash(key)

    cipher = AES256CTR(hashed_key[0:32])
    nonce = cipher.get_readable_nonce()
    ciphertext = cipher.encrypt(data)

    json_data = {
        "origin": origin,
        "decrypt_info": {
            "nonce": nonce,
            "ciphertext": ciphertext
        }
    }

    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    #! write operation overwrites entire file
    with open("../local/encrypted_passwords.json", "w") as file: #TODO: What if file doesn't exist?
        json.dump(json_data, file, indent=4)

    
if __name__ == "__main__":
    main()