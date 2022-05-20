class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """
    first -> foo -> bar -> last -> None
    """

    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first == self.last == new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp


q = Queue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.print_queue()
