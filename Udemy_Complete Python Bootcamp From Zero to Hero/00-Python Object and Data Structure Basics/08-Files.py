

# myfile = open(r'E:\python_work\Udemy_Complete Python Bootcamp From Zero to Hero\00-Python Object and Data Structure Basics\test.txt')




# print(myfile.read())

# myfile.seek(0)

# print(myfile.read())

# myfile.seek(0)

# print(myfile.readlines())

# myfile.close()



# myfile = open(r'E:\python_work\Udemy_Complete Python Bootcamp From Zero to Hero\00-Python Object and Data Structure Basics\test.txt', "w+")

# myfile.write("writing")

# myfile.readlines()

# myfile.close()



# myfile = open(r'E:\python_work\Udemy_Complete Python Bootcamp From Zero to Hero\00-Python Object and Data Structure Basics\test.txt', "a+")

# myfile.write("\nthis is text being appended")

# myfile.write("\n another line")

# myfile.seek(0)

# print(myfile.readlines())

# myfile.close()

for line in open(r'E:\python_work\Udemy_Complete Python Bootcamp From Zero to Hero\00-Python Object and Data Structure Basics\test.txt'):
    print(line)
