import json
import os

filename = "/username.json"

dirname = os.path.dirname(__file__)

with open(dirname + filename) as file_obj:
    username = json.load(file_obj)
    print("welcome back, " + username)