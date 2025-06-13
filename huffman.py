"""
venn mani abhiram reddy
css-120
project-hoffman
Implements a Huffman decoding tree to decode a 
binary sequence using preorder and inorder traversals.

"""
class Node:
    """Represents a node in the Huffman decoding tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class HuffmanDecoder:
    """Manages the construction and decoding of a Huffman tree.
    
    """
    def __init__(self):
        self.root = None
    
    def build_tree(self, preorder, inorder):
        """Recursively constructs the Huffman tree from 
        preorder and inorder traversals.
        PAPPAMAETRS: The build_tree method takes three parameters
        self, the HuffmanDecoder instance; preorder, 
        a list of integers representing
          the preorder traversal of the Huffman tree;
            and inorder, a list of integers
            representing the inorder traversal of the tree.
        ARRGRS: Arguments include self, the instance like decoder;
          preorder and inorder
        RETURN: The method returns a Node object representing
          the root of the constructed Huffman tree,
            or None if preorder or inorder is empty."""
        if not preorder or not inorder:
            return None
        # Root is the first element in preorder
        root_value = preorder[0]
        root = Node(root_value)
        # Find root in inorder to split into left and right subtrees
        root_index = 0
        for i in range(len(inorder)):
            if inorder[i] == root_value:
                root_index = i
                break
        # Left subtree: elements before root in inorder
        left_inorder = []
        for i in range(root_index):
            left_inorder.append(inorder[i])
        # Right subtree: elements after root in inorder
        right_inorder = []
        for i in range(root_index + 1, len(inorder)):
            right_inorder.append(inorder[i])
        # Left preorder: elements after root, matching length of left_inorder
        left_preorder = []
        for i in range(1, 1 + len(left_inorder)):
            left_preorder.append(preorder[i])
        # Right preorder: remaining elements
        right_preorder = []
        for i in range(1 + len(left_inorder), len(preorder)):
            right_preorder.append(preorder[i])
        # Recursively build left and right subtrees
        root.left = self.build_tree(left_preorder, left_inorder)
        root.right = self.build_tree(right_preorder, right_inorder)
        return root
    
    def postorder_traversal(self, node, result):
        """Performs a postorder traversal 
        of the tree and collects node values."""
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)
    
    def decode_sequence(self, sequence):
        """Decodes a binary sequence using the Huffman tree.
        PAPPAMAETRS: The decode_sequence method takes two parameters: self,
          the HuffmanDecoder instance, and sequence, a string of binary 
          digits ('0' or '1') representing the encoded sequence to decode.
        ARRGRS: Arguments include self, the instance like decoder,
          and sequence, for a binary sequence.
    RETURN: The method returns a list of integers,
      each representing a decoded value from the Huffman tree,
        returns an empty list if the tree’s root is None.
        """

        if not self.root:
            return []
        result = []
        current = self.root
        for bit in sequence:
            # Move left for '0', right for '1'
            if bit == '0':
                current = current.left
            else:
                current = current.right
            # If at a leaf node, add value to result and reset to root
            if current and not current.left and not current.right:
                result.append(current.value)
                current = self.root
        return result

def main():
    """Main function to read input, process data, and output results."""
    # Read input file name
    filename = input('Input file: ')
    # Open and read the file
    file = open(filename, 'r')
    # Read three lines: preorder, inorder, and encoded sequence
    preorder_line = file.readline().strip().split()
    preorder = []
    for num in preorder_line:
        preorder.append(int(num))
    inorder_line = file.readline().strip().split()
    inorder = []
    for num in inorder_line:
        inorder.append(int(num))
    sequence = file.readline().strip()
    file.close()
    
    # Create Huffman decoder and build tree
    decoder = HuffmanDecoder()
    decoder.root = decoder.build_tree(preorder, inorder)
    
    # Get postorder traversal
    postorder = []
    decoder.postorder_traversal(decoder.root, postorder)
    output = ''
    for i in range(len(postorder)):
        if i > 0:
            output += ' '
        output += str(postorder[i])
    print(output)
    
    # Decode the sequence and print result
    decoded = decoder.decode_sequence(sequence)
    output = ''
    for num in decoded:
        output += str(num)
    print(output)

# Run the program
main()