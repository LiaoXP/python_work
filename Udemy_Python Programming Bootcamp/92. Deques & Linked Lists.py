# class Deque:
#     def __init__(self):
#         self.deque = []

#     def add_front(self, data):
#         self.deque.append(data)

#     def add_rear(self, data):
#         self.deque.insert(0, data)

#     def is_empty(self):
#         return self.deque == []

#     def remove_front(self):
#         if self.is_empty():
#             return "empty deque"
#         else:
#             return self.deque.pop()

#     def remove_rear(self):
#         if self.is_empty():
#             return "empty deque"
#         else:
#             return self.deque.pop(0)

#     def size(self):
#         return len(self.deque)

#     def check_palindrome(self):
#         is_palindrome = True
#         while self.size() > 1 and is_palindrome:
#             front = self.remove_front()
#             rear = self.remove_rear()
#             if front != rear:
#                 is_palindrome = False
#         return is_palindrome




# d_1 = Deque()
# d_1.add_front("dog")
# d_1.add_rear("cat")
# d_1.add_rear("mouse")
# print(f"front : {d_1.remove_front()}")
# print(f"rear : {d_1.remove_rear()}")
# print(f"size : {d_1.size()}")

# d_2 = Deque()
# word = "racecar"
# for i in word:
#     d_2.add_rear(i)
# print(f"palindrome : {d_2.check_palindrome()}")

# word_2 = "zero"
# for i in word_2:
#     d_2.add_rear(i)
# print(f"palindrome : {d_2.check_palindrome()}")



class Node:
    def __init__(self):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def remove(self, search_value):
        current_node = self.head

        prev_node = None
        data_found = False

        while not data_found:
            if current_node.get_data() == search_value:
                data_found = True
            else:
                prev_node = current_node
                current_node = prev_node.get_next()

        if prev_node is None:
            self.head = current_node.get_next()
        else:
            prev_node.set_next(current_node.get_next())