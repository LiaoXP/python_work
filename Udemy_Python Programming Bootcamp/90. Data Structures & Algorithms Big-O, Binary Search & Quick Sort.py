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


def binary_search(value: int):
    list_size = len(list_1)
    low_index = 0
    high_index = list_size - 1
    while low_index <= high_index:
        
