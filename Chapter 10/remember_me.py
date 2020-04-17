import json
import os

filename = "/username.json"

dirname = os.path.dirname(__file__)

complete_file_path = dirname + filename

def get_stored_username():
    

    try:
        with open(complete_file_path) as file_obj:
            username = json.load(file_obj)
    except FileNotFoundError:
         return None
    else:
        return username   

def greet_user():
    
    username = get_stored_username()

    if username:
        print("welcome back, " + username)
    else:
        username = input("what is ur name? ")

        with open(complete_file_path, "w") as file_obj:
            json.dump(username, file_obj)
            print("we will remember you when u come back, " + username)
    
        

greet_user()


