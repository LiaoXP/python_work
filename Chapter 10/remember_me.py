import json
import os

filename = "/username.json"

dirname = os.path.dirname(__file__)

complete_file_path = dirname + filename

try:
    with open(complete_file_path) as file_obj:
        username = json.load(file_obj)

        
except FileNotFoundError:
    username = input("what is ur name? ")

    with open(complete_file_path, "w") as file_obj:
        json.dump(username, file_obj)
        print("we will remember you when u come back, " + username)
else:
    print("welcome back, " + username)


