import random
def bubble_sort(list):
    unsorted_until_index = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if list[i] > list[i + 1]:
                sorted = False
                list[i], list[i + 1] = list[i + 1], list[i]
        unsorted_until_index = unsorted_until_index - 1

    return list

list = []
for i in range(10):
    list.append(random.randint(1, 1000))

print(list)
print(bubble_sort(list))

