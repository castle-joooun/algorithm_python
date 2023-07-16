class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is not None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, idx):
        current = self.haed
        for _ in range(idx):
            if current.next is not None:
                current = current.next
        return current

    def insert(self, idx, value):
        current = self.haed
        prev = None
        for _ in range(idx):
            prev = current
            current = current.next
        new_node = Node(value, current.next)
        prev.next = new_node

    def remove(self, idx):
        current = self.head
        prev = None
        for _ in range(idx):
            prev = current
            current = current.next
        prev.next = current


