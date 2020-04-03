import os

fileName = "\programming.txt"

dir_path = os.path.dirname(__file__)

with open(dir_path + fileName, "a") as file_object:
    file_object.write("i love programming\n")
    file_object.write("i love making application\n")