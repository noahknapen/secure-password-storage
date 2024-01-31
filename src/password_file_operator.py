import json

class PasswordFileOperator:
    def __init__(self, json_file_path):
        self.__path = json_file_path #TODO: check if file exists

    def __get_file_contents(self):
        try:
            with open(self.__path, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}


    def __write_file(self, data):
        with open(self.__path, "w") as file:
            json.dump(data, file, indent=4)

    #TODO: check if origin already exists with username combination
    def new_origin_entry(self, origin, username, nonce, ciphertext):
        new_json_data = {
            "username": username,
            "decrypt_info": {
                "nonce": nonce,
                "ciphertext": ciphertext
            }
        }

        file_json_data = self.__get_file_contents()
        file_json_data[origin] = new_json_data
        self.__write_file(file_json_data)

    def overwrite_origin_entry(self, origin, new_nonce, new_ciphertext):
        file_json_data = self.__get_file_contents()
        self.new_origin_entry(origin, file_json_data[origin]["username"], new_nonce, new_ciphertext)            
