import os

# file_path = "\pi_digits.txt"

# dir_path = os.path.dirname(__file__)

# with open(dir_path + file_path) as file_object:
#     lines = file_object.readlines()

# pi_string = ""

# for line in lines:
#     pi_string += line.rstrip()

# print(pi_string)

# print(len(pi_string))








file_path = "\pi_million_digits.txt"

dir_path = os.path.dirname(__file__)

with open(dir_path + file_path) as file_object:
    lines = file_object.readlines()

pi_string = ""

for line in lines:
    pi_string += line.strip()

birthday = input("Enter ur birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("ur birthday appears in the first million digits of pi")
else:
    print("ur birthday does not appear in the first million digits of pi")

