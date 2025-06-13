class Queue:
    def __init__(self):
        self.items = ""
    
    def enqueue(self, item):
        self.items += item
    
    def dequeue(self):
        if self.is_empty():
            return None
        item = self.items[0]
        self.items = self.items[1:]
        return item
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __str__(self):
        return self.items