class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None 

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while True:
            if temp is None:
                return False
            if temp.value == value:
                return True
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

bst = BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(3)

print(bst.min_value_node(bst.root).value)
# print(bst.contains(1))
# print(bst.root.value)
# print(bst.root.left.value)
# print(bst.root.right.value)
