class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        return self._items.pop()

    def is_empty(self):
        return self._items == []
    
    def __str__(self):
        return str(self._items)
def decimal2binary(n):
    stack = Stack()
    if n == 0:
        return "0"
    while n:
        stack.push(str(n % 2))
        n //= 2
    binary_str = ''
    while not stack.is_empty():
        binary_str += stack.pop()
    return binary_str
