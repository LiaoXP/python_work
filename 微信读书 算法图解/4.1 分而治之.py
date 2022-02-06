# #4.1 请编写前述sum函数的代码。
# def sum(arr):
#     if len(arr) == 0:
#         return 0
#     elif len(arr) == 1:
#         return arr[0]
#     else:
#         return sum(arr[0:len(arr) - 1]) + arr[len(arr) - 1]
# print(sum(range(1,101)))

# #4.2 编写一个递归函数来计算列表包含的元素数。
# print(len([2,4,6]))
# def listQty(lst):
#     if lst[0] == None:
#         return 0
#     else:
#         return listQty(lst.pop()) + 1
# print(listQty([2,4,6]))

#4.3 找出列表中最大的数字。
def find_the_biggest(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        biggest = lst[len(lst) - 1]
        if biggest >= find_the_biggest(lst[0:len(lst) - 1]):
            return biggest
        else:
            return find_the_biggest(lst[0:len(lst) - 1])
print(find_the_biggest([8,5,2]))