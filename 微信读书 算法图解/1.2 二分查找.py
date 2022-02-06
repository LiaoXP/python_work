import random

# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1

#     while low <= high:
#         mid = int((low + high)/2)
#         guess = list[mid]
#         if guess == item:
#             return mid
#         elif guess < item:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return None

# def quick_sort(list):
#     if len(list) < 2:
#         return list
#     else:
#         pivot_index = random.randint(0, len(list) - 1)
#         pivot = list[pivot_index]
#         less_than_pivot = []
#         more_than_pivot = []
#         equal_to_pivot = []

#         #list[0], list[pivot_index] = list[pivot_index], list[0]

#         for i in range(0, len(list)):
#             if list[i] < pivot:
#                 less_than_pivot.append(list[i])
#             elif list[i] > pivot:
#                 more_than_pivot.append(list[i])
#             else:
#                 equal_to_pivot.append(list[i])
#         return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(more_than_pivot)

# list1 = [1, 2, 28, 31, 32, 39, 54, 57, 71, 87, 89, 96, 97, 125, 153, 154, 156, 178, 179, 189, 200, 205, 207, 212, 235, 239, 244, 265, 267, 271, 283, 293, 316, 319, 323, 362, 364, 377, 381, 386, 396, 402, 409, 427, 430, 437, 440, 449, 468, 499, 519, 525, 532, 546, 553, 559, 
# 572, 576, 602, 603, 604, 610, 616, 628, 635, 641, 642, 644, 647, 648, 655, 662, 679, 724, 730, 733, 741, 743, 753, 760, 768, 771, 778, 829, 841, 842, 851, 855, 871, 915, 936, 952, 953, 962, 963, 965, 966, 973, 990, 1000]
# for i in range(100):
#     while True:
#         new_int = random.randint(1, 1000)
#         if new_int in list1:
#             continue
#         else:
#             list1.append(new_int)
#             break


# print((list1))

# print((quick_sort(list1)))

# print(binary_search(list1, 990))

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
