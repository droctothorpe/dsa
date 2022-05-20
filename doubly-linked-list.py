class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.tail = self.head = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            temp.previous = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.tail = None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - index):
                temp = temp.previous

        return temp

    def set_value(self, index, value):
        node = self.get(index)
        if not node:
            return False
        node.value = value

        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        after = self.get(index)
        before = after.previous
        before.next = new_node
        new_node.previous = before
        new_node.next = after
        after.previous = new_node
        self.length += 1

        return True

    def remove(self, index):
        temp = self.get(index)
        if not temp:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        else:
            temp.next.previous = temp.previous
            temp.previous.next = temp.next
            temp.next = None
            temp.previous = None
        self.length -= 1

        return temp


d = DoublyLinkedList(1)
d.append(2)
d.append(3)
d.remove(1)
d.print_list()
