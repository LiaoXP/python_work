import os

file_path = "\pi_digits.txt"

dir_path = os.path.dirname(__file__)

with open(dir_path + file_path) as file_object:
    lines = file_object.readlines()

pi_string = ""

for line in lines:
    pi_string += line.strip()

print(pi_string)

print(len(pi_string))