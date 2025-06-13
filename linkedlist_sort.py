"""
Author: mani abhiram reddy
Date: 03-04-2025
Description: This program reads integers from a file, creates a linked list,
sorts it in descending order, and prints the sorted list.
"""
class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def __str__(self):
        """
        Returns a string representation of the node's value.
        Parameters: None.
        Returns:
            str: The string representation of the node's value.
        """
        return str(self._value)

class LinkedList:
    def __init__(self):
        self._head = None

    def add(self, value):
        """
        Adds a new node with the given
        value to the end of the linked list.
        Parameters:
            value: The value to be added to the linked list.
        Returns: None.
        """
        new_node = Node(value)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current._next is not None:
                current = current._next
            current._next = new_node

    def sort_ascending(self):
        """
        Sorts the linked list in ascending
        order based on the _value attribute of the nodes.
        The nodes are moved from the original
        list to a new list that is kept sorted.
        """
        sorted_list = LinkedList()
        # Continue until the original list is empty
        while self._head is not None:
            min_node = self._head
            prev_min = None
            current = self._head
            prev = None
            # Traverse the list to find the minimum node
            while current is not None:
                if current._value < min_node._value:
                    min_node = current
                    prev_min = prev
                prev = current
                current = current._next
            if prev_min is None:
                self._head = min_node._next
            else:
                prev_min._next = min_node._next
            if sorted_list._head is None:
                sorted_list._head = min_node
                min_node._next = None
            else:
                min_node._next = sorted_list._head
                sorted_list._head = min_node
        # Update the original list to point to the sorted list
        self._head = sorted_list._head

    def __str__(self):
        """
        Returns a string representation 
        of the linked list.
        Parameters: None.
        Returns:
            str: A string in the format 
            "List[ value1; value2; ... ]".
        """
        result = "List[ "
        current = self._head
        # Traverse the list and append each value
        # to the result string
        while current is not None:
            result += str(current._value) + "; "
            current = current._next
        result += "]"
        return result
filename = input()
file = open(filename, "r")
data = file.read().strip().split()
file.close()  # Close the file
linked_list = LinkedList()
# Add each value to the linked list
for value in data:
    linked_list.add(int(value))
linked_list.sort_ascending()
print(linked_list)