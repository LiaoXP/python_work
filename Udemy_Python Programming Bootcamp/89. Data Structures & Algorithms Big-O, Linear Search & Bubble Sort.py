import random
import time

list_1 = []
start_time = 0
end_time = 0



def generate_rand_list(max_size):
    new_list = []
    for i in range(0, max_size):
        new_list.append(random.randint(1, 99))
    return new_list

def bubble_sort():
    #print(list_1)
    list_size = len(list_1)
    #print(range(list_size))
    for i in range(list_size):
        #print(str(i) + " round")
        for j in range(list_size - i - 1):
            if list_1[j] > list_1[j+1]:
                list_1[j], list_1[j+1] = list_1[j+1], list_1[j]
            # for k in list_1:
            #     print(k, end=", ")
            #print(list_1)
            #print()

list_1 = generate_rand_list(10)
start_time = time.time()
bubble_sort()
print(f"{time.time() - start_time}")

list_1 = generate_rand_list(100)
start_time = time.time()
bubble_sort()
print(f"{time.time() - start_time}")

list_1 = generate_rand_list(1000)
start_time = time.time()
bubble_sort()
print(f"{time.time() - start_time}")



# list_1 = generate_rand_list(10)

# def add_item_to_list(num):
#     list_1.append(num)

# def linear_search(val):
#     val_found = "Value Not Found"
#     for i in list_1:
#         if i == val:
#             val_found = "Value Found"
#     print(val_found)

# print("testing linear search")
# list_1 = generate_rand_list(10)
# start_time = time.time()
# linear_search(10000)
# print(f"{time.time() - start_time} seconds")

# print("testing linear search")
# list_1 = generate_rand_list(1000)
# start_time = time.time()
# linear_search(10000)
# print(f"{time.time() - start_time} seconds")

# print("testing linear search")
# list_1 = generate_rand_list(100000)
# start_time = time.time()
# linear_search(10000)
# print(f"{time.time() - start_time} seconds")