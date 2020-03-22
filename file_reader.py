file_path = r"C:\Users\123\Documents\GitHub\python_work\pi_digits.txt"

with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

with open(file_path) as file_object:
    for line in file_object:
        print(line)