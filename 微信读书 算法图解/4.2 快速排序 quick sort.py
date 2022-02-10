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

