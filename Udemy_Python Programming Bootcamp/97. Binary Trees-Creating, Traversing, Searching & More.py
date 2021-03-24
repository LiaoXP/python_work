class Node:
    def __init__(self, key = 0, name = ""):
        self.key = key
        self.name = name

        self.left_child = None
        self.right_child = None

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
                parent = focus_node

                if key < focus_node.key:
                    focus_node = focus_node.left_child

                    if focus_node is None:
                        parent.left_child = new_node

                        return True
                else:
                    focus_node = focus_node.right_child

                    if focus_node is None:
                        parent.right_child = new_node

                        return True

    def in_order_traverse(self, focus_node):
        if focus_node is not None:
            self.in_order_traverse(focus_node.left_child)
            print(focus_node)
            self.in_order_traverse(focus_node.right_child)

    def preorder_traverse(self, focus_node):
        if focus_node is not None:
            print

