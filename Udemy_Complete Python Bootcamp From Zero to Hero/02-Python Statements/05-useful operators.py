# print(list(range(0, 10, 2)))

# index_count = 0

# for letter in "abcde":
#     print("at index {} the letter is {}".format(index_count, letter))
#     index_count += 1

# for i,letter in enumerate("abcde"):
#     print("at index {} the letter is {}".format(i, letter))

# index_count = 0

# for letter in "liao":
#     print(f"at index {index_count} the letter is {letter}")
#     index_count += 1

# for i,letter in enumerate("liao", 1):
#     print(f"at index {i} the letter is {letter}")



# print(list(enumerate("liao")))

# mylist1 = [1,2,3,4,5]
# mylist2 = ['a','b','c','d','e', 'f']
# mylist3 = ['a','b','c','d','e', 'f']

# print(list(zip(mylist1, mylist2, mylist3)))

# for item1, item2, item3 in zip(mylist3, mylist2, mylist1):
#     print(f"first item {item1}, second item {item2}, third item {item3}")


print('x' in ['y','z'])

from random import shuffle, randint


mylist = [10,20,30,40,100]
shuffle(mylist)

print(mylist)

print(randint(0, 1000))

print(input("key in sth.: "))


