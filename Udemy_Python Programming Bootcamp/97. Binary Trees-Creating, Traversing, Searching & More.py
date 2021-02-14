class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, key, name):
        new_node = Node(key, name)
        if self.root is None:
            self.root = new_node
        else:
            focus_node = self.root
            while True:
                

class Node:
    def __init__(self, key=0, name=""):
        self.key = key
        self.name = name
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f"{self.name} has the key {self.key}"