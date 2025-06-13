class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.friends = LinkedList()  # Each node has its own friend list

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count