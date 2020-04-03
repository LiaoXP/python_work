import os

filename = "/alice.txt"

dir_name = os.path.dirname(__file__)

try:

    with open(dir_name + filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "the file " + filename + " does not exist"

    print(msg)
else:
    words = contents.split()

    num_words = len(words)

    print("the file " + filename + " has about " + str(num_words) + " words")