import random

def generate_rand_list(max_size):
    new_list = []
    for i in range(0, max_size):
        new_list.append(random.randint(1, 99))
    return new_list
#quick sort
list_to_be_sorted = generate_rand_list(10)
print(list_to_be_sorted)


# follow udemy course Python Programming Bootcamp's version,
# pass start and end position of the array to the function as parameters,
# just swap members of the array within the array, this approach saves space, but not easy to understand, not straight forward
def quick_sort_swap_within_array(start, end):
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

# 相比上面那个方法，这个实现要直观得多，几乎就是快速排序算法原理描述直接翻译成代码（来自“算法图解”这本书）
# 但是组成子数组的两个数组遍历似乎有重复操作
# 而且这种方法会多创建很多数组的副本，比上面的方法更占空间
def quick_sort_create_new_array(list_to_be_sorted):
    if len(list_to_be_sorted) < 2:
        return list_to_be_sorted
    else:
        pivot = list_to_be_sorted[0]
        less = [i for i in list_to_be_sorted[1:] if i <= pivot]
        greater = [i for i in list_to_be_sorted[1:] if i > pivot]
        
        return quick_sort_create_new_array(less) + [pivot] + quick_sort_create_new_array(greater)


#quick_sort_swap_within_array(0, len(list_to_be_sorted) - 1)
print(quick_sort_create_new_array(list_to_be_sorted))
print(list_to_be_sorted)
