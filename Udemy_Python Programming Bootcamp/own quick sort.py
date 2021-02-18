import random

def generate_rand_list(max_size):
    new_list = []
    for i in range(0, max_size):
        new_list.append(random.randint(1, 99))
    return new_list
#quick sort
list_to_be_sorted = generate_rand_list(5)
print(list_to_be_sorted)

def quick_sort(start, end):
    if end - start == 1:
        print("end - start == 1")
        if list_to_be_sorted[start] > list_to_be_sorted[end]:
            print("list_to_be_sorted[start] > list_to_be_sorted[end]")
            list_to_be_sorted[start], list_to_be_sorted[end] = list_to_be_sorted[end], list_to_be_sorted[start]
            print(list_to_be_sorted)
        return
    elif end > start:
        print("end > start")
        
        low = start + 1
        high = end
        pivot = list_to_be_sorted[start]
        print(f"end = {end}, start = {start}, low = {low}, high = {high}, pivot = {pivot}")
        while True:
            while low <= high and list_to_be_sorted[low] <= pivot:
                low = low + 1
            while high >= low and list_to_be_sorted[high] >= pivot:
                high = high - 1
            if low <= high:
                list_to_be_sorted[low], list_to_be_sorted[high] = list_to_be_sorted[high], list_to_be_sorted[low]
                low = low + 1
                high = high - 1
                print(list_to_be_sorted)
            else: # low == high
                list_to_be_sorted[start], list_to_be_sorted[low] = list_to_be_sorted[low], list_to_be_sorted[start]
                print(list_to_be_sorted)
                quick_sort(start, low - 1)
                quick_sort(high + 1, end)
                break
    else:
        return
quick_sort(0, len(list_to_be_sorted) - 1)
print(list_to_be_sorted)
