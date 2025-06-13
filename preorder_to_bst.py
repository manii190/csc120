class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        if self.left:
            left = self.left
        else:
            left = None
        right = self.right if self.right else None
        return f"({self.data} {left} {right})"

def preorder_to_bst(preorder):
    if not preorder:
        return None
    root_val = preorder[0]
    left_preorder = []
    right_preorder = []
    for val in preorder[1:]:
        if val < root_val:
            left_preorder.append(val)
        else:
            right_preorder.append(val)
    left_subtree = preorder_to_bst(left_preorder)
    right_subtree = preorder_to_bst(right_preorder)
    return BinarySearchTree(root_val, left_subtree, right_subtree)