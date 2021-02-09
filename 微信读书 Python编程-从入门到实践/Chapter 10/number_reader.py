import json
import os

filename = "/numbers.json"

dirname = os.path.dirname(__file__)

with open(dirname + filename) as file_object:
    numbers = json.load(file_object)
print(numbers)