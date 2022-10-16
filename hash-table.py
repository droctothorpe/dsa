class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def _hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self._hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self._hash(key)
        if self.data_map[index] is not None:
            for element in self.data_map[index]:
                if element[0] == key:
                    return element[1]
        return None

    def keys(self):
        keys = []
        for i in self.data_map:
            if i is not None:
                for j in i:
                    keys.append(j[0])
        return keys


ht = HashTable()
ht.set_item("bolts", 1400)
ht.set_item("washers", 50)
ht.set_item("lumber", 70)
ht.print_table()
# print("lumbar:", ht.get_item("lumber"))
# print("foo:", ht.get_item("foo"))
# print("bolts", ht.get_item("bolts"))
print(ht.keys())
