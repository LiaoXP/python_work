<<<<<<< HEAD
# def quickSort(array):
#     if len(array) < 2:
#         return array   #基线条件：为空或只包含一个元素的数组是“有序”的
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]   #由所有小于等于基准值的元素组成的子数组
#         print("after less:" + str(array))
#         greater = [i for i in array[1:] if i > pivot]   #由所有大于等于基准值的元素组成的子数组
#         return quickSort(less) + [pivot] + quickSort(greater)

# print(quickSort([10,5,2,3]))


def quickSort(array):
    if len(array) < 2:
        return array   #基线条件：为空或只包含一个元素的数组是“有序”的
    else:
        pivot = array[0]
        less = []
        greater = []
        for i in array[1:]:
            if i <= pivot:
                less.append(i)
            else:
                greater.append(i)
        return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort([10,5,2,3]))

=======
def quicksort(array):
    if len(array) < 2:
        return array # 基线条件：为空或只包含一个元素的数组是“有序”的
    else:
        pivot = array[0] # 递归条件
        less = [i for i in array[1:] if i <= pivot] # 由所有小于等于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot] # 由所有大于基准值的元素组成的子数组

        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10,5,3,2]))
>>>>>>> 3088f5db0b2446fe1b1b1fe20b58936b34e8663c
