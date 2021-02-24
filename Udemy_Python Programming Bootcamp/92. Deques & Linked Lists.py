class Deque:
    def __init__(self):
        self.deque = []

    def add_front(self, data):
        self.deque.append(data)

    def add_rear(self, data):
        self.deque.insert(0, data)

    def is_empty(self):
        return self.deque == []

    def remove_front(self):
        if self.is_empty():
            return "empty deque"
        else:
            return self.deque.pop()

    def remove_rear(self):
        if self.is_empty():
            return "empty deque"
        else:
            return self.deque.pop(0)

    def size(self):
        return len(self.deque)




d_1 = Deque()
d_1.add_front("dog")
d_1.add_rear("cat")
d_1.add_rear("mouse")
print(f"front : {d_1.remove_front()}")
print(f"rear : {d_1.remove_rear()}")
print(f"size : {d_1.size()}")