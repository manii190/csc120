class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def add(self, val):
        if self.value is None:
            self.value = val
        elif val < self.value:
            if self.left is None:
                self.left = BinarySearchTree(val)
            else:
                self.left.add(val)
        else:
            if self.right is None:
                self.right = BinarySearchTree(val)
            else:
                self.right.add(val)
    
    def find(self, val):
        if self.value is None or self.value == val:
            return self
        elif val < self.value and self.left is not None:
            return self.left.find(val)
        elif val > self.value and self.right is not None:
            return self.right.find(val)
        return None
    
    def __str__(self):
        if self.value is None:
            return "None"
        left_str = str(self.left) if self.left else "None"
        right_str = str(self.right) if self.right else "None"
        return "({} {} {})".format(self.value, left_str, right_str)