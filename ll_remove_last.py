class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
    
    def ll_remove_last(self):
        if self._head is None:
            return None
        if self._head == self._tail:
            data = self._head.data
            self._head = None
            self._tail = None
            return data
        current = self._head
        while current.next != self._tail:
            current = current.next
        data = self._tail.data
        self._tail = current
        self._tail.next = None
        return data