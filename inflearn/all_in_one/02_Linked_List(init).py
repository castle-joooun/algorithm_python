class Node:
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

            current = self.head
            while current.next:
                current.next.prev = current
                current = current.next

    def get(self, idx):
        current = self.head
        for _ in range(idx):
            if current.next:
                current = current.next
        return current.value

    def insert(self, idx, value):
        current = self.head
        for _ in range(idx):
            current = current.next
        new_node = Node(value, current, current.prev)
        current.prev.next = new_node

    def remove(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next

        print(current.prev)
        current.prev.next = current.next


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print(ll.get(1))
ll.insert(1, 5)
print(ll.get(1))
ll.remove(1)
print(ll.get(1))