import json

class PasswordFileOperator:
    def __init__(self, json_file_path):
        self.__path = json_file_path #TODO: check if file exists

    def add_entry(self, origin, username, nonce, ciphertext):
        file_json_data = self.__get_file_contents()
        if file_json_data.get(origin) == None:
            self.__new_entry(origin, username, nonce, ciphertext)
        elif username not in [entry["username"] for entry in file_json_data[origin]]:
            self.__append_entry(origin, username, nonce, ciphertext)
        else:
            self.__overwrite_entry(origin, username, nonce, ciphertext)

    """Returns a dictionary consisting of the nonce and ciphertext for the given origin and username
    """
    def retrieve_entry(self, origin, username):
        file_json_data = self.__get_file_contents()
        for entry in file_json_data[origin]:
            if entry["username"] == username:
                return entry["decrypt_info"]

    #######################
    ### PRIVATE METHODS ###
    #######################

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
    def __new_entry(self, origin, username, nonce, ciphertext):
        new_json_data = {
            "username": username,
            "decrypt_info": {
                "nonce": nonce,
                "ciphertext": ciphertext
            }
        }

        file_json_data = self.__get_file_contents()
        file_json_data[origin] = [new_json_data]
        self.__write_file(file_json_data)

    def __append_entry(self, origin, username, nonce, ciphertext):
        new_json_data = {
            "username": username,
            "decrypt_info": {
                "nonce": nonce,
                "ciphertext": ciphertext
            }
        }

        file_json_data = self.__get_file_contents()
        file_json_data[origin].append(new_json_data)
        self.__write_file(file_json_data)

    def __overwrite_entry(self, origin, username, new_nonce, new_ciphertext):
        file_json_data = self.__get_file_contents()

        for entry in file_json_data[origin]:
            if entry["username"] == username:
                entry["decrypt_info"] = {
                    "nonce": new_nonce,
                    "ciphertext": new_ciphertext
                }

        self.__write_file(file_json_data)
