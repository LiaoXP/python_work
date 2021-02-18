import random
import time

list_1 = []
start_time = 0
end_time = 0

def partition(start, end):
    pivot = list_1[start]
    low = start + 1
    high = end
    while True:
        while low <= high and list_1[high] >= pivot:
            high = high - 1
        while low <= high and list_1[low] <= pivot:
            low = low + 1
        if low <= high:
            list_1[low], list_1[high] = list_1[high], list_1[low]
        else:
            break
    list_1[start], list_1[high] = list_1[high], list_1[start]
    return high

def quick_sort(start, end):
    for k in list_1:
        print(k, end=", ")
    print()
    if start >= end:
        return
    part = partition(start, end)
    quick_sort(start, part-1)
    quick_sort(part+1, end)

def generate_rand_list(max_size):
    new_list = []
    for i in range(0, max_size):
        new_list.append(random.randint(1, 99))
    return new_list


def binary_search(value: int):
    list_size = len(list_1)
    low_index = 0
    high_index = list_size - 1
    while low_index <= high_index:
        mid_index = int((high_index + low_index) / 2)
        if list_1[mid_index] < value:
            low_index = mid_index + 1
        elif list_1[mid_index] > value:
            high_index = mid_index - 1
        else:
            print(f"Found a match for {value} at index {mid_index}")
            low_index = high_index + 1

list_1 = generate_rand_list(10)
quick_sort(0, len(list_1) - 1)
