class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    # top -> foo -> bar -> None
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp


s = Stack(1)
s.push(2)
s.push(3)
s.print_stack()
print("Popped:", s.pop().value)
s.print_stack()
