import os

# file_path = r"C:\Users\123\Documents\GitHub\python_work\pi_digits.txt"

dir_path = os.path.dirname(__file__)

file_path = "/pi_digits.txt"

# with open(dir_path + file_path) as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

# with open(dir_path + file_path) as file_object:
#     for line in file_object:
#         print(line.rstrip())

with open(dir_path + file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
    