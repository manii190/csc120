class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
    
    def value(self):
        return self._value
    
    def next(self):
        return self._next
        
    def __str__(self):
        return str(self._value) + "; "
    
class LinkedList:
    def __init__(self):
        self._head = None

    def add(self, node):
        node._next = self._head
        self._head = node
        
    def __str__(self):
        string = 'List[ '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        string += ']'
        return string
    
    def sum(self):
        total = 0
        curr_node = self._head
        while curr_node is not None:
            total += curr_node.value()
            curr_node = curr_node.next()
        return total
ll = LinkedList()
ll.add(Node(1))
ll.add(Node(3))
ll.add(Node(2))

print(ll.sum())