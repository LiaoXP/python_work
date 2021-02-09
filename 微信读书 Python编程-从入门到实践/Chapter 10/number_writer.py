import json
import os

numbers = [2,3,5,7,11,13]

filename = "/numbers.json"

dirname = os.path.dirname(__file__)

with open(dirname + filename, "w") as file_object:
    json.dump(numbers, file_object)