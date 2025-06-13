class Stack:
    def __init__(self):  
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None  

    def is_empty(self):
        return len(self.items) == 0
    
    def __str__(self):  
        return str(self.items)

def is_balanced(symbols):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in symbols:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            top = stack.pop()
            if top is None or top != pairs[char]:
                return False
    return stack.is_empty()

