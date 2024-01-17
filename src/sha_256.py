from Crypto.Hash import SHA3_256

class SHA256:
    def __init__(self):
        self.hash_object = SHA3_256.new()
        self.hash_object.digest_size = 32

    def get_binary_hash(self, data):
        #binary_data = ''.join(format(ord(i), 'b') for i in data)
        binary_data = data.encode('utf-8')
        self.hash_object.update(binary_data)
        return self.hash_object.digest()
    
    def get_hex_hash(self, data):
        #binary_data = ''.join(format(ord(i), 'b') for i in data)
        binary_data = data.encode('utf-8')
        self.hash_object.update(binary_data)
        return self.hash_object.hexdigest()

    def reset_hash_object(self):
        self.hash_object = SHA3_256.new()