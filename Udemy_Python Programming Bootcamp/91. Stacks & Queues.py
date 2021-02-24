import time

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, data):
#         self.stack.insert(0, data)

#     def is_empty(self):
#         return self.stack == []

#     def pop(self):
#         if self.is_empty():
#             return "stack empty"
#         return self.stack.pop(0)

#     def peek(self):
#         return self.stack[0]

#     def size(self):
#         return len(self.stack)

#     def reverse_string(self):
#         while True:
#             if len(self.stack) == 0:
#                 break
#             else:
#                 print(self.stack.pop(0), end="")

# s_1 = Stack()
# s_1.push("cat")
# s_1.push("dog")
# print(s_1.size())
# print(s_1.peek())
# print(s_1.pop())
# print(s_1.pop())
# print(s_1.pop())

# s_1.push("c")    
# s_1.push("a") 
# s_1.push("t") 
# s_1.reverse_string()


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)

    def is_empty(self):
        return self.queue == []

    def dequeue(self):
        if self.is_empty():
            return "queue empty"
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def wait_your_turn(self):
        while True:
            if len(self.queue) == 0:
                break
            else:
                print(f"{self.dequeue()} takes its turn")
                time.sleep(3)
q_1 = Queue()
q_1.enqueue("cat")
q_1.enqueue("dog")
print(q_1.size())
print(q_1.dequeue())
print(q_1.dequeue())
print(q_1.dequeue())

q_1.enqueue("cat")
q_1.enqueue("dog")
q_1.wait_your_turn()