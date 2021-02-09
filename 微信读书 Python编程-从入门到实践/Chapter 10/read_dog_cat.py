import os

filepathdog = "\dogs.txt"

filepathCat = "\cats.txt"

dirpath = os.path.dirname(__file__)

try:
    with open(dirpath + filepathCat) as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())

    with open(dirpath + filepathdog) as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())
except FileNotFoundError:
    print("file does not exist")
