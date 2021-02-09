import os

def count_words(filename):
    """count number of words in a file"""
    dir_name = os.path.dirname(__file__)

    try:

        with open(dir_name + "/" + filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = "the file " + filename + " does not exist"

        # print(msg)

        pass
    else:
        words = contents.split()

        num_words = len(words)

        print("the file " + filename + " has about " + str(num_words) + " words")



filenames = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt"]

for filename in filenames:
    count_words(filename)