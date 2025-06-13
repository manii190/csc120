import csv
import string

class Node:
    def __init__(self, word):
        self._word = word
        self._count = 1
        self._next = None

    def word(self):
        return self._word

    def count(self):
        return self._count

    def next(self):
        return self._next

    def set_next(self, target):
        self._next = target

    def incr(self):
        self._count += 1

    def __str__(self):
        return "{} : {}".format(self._word, self._count)

class LinkedList:
    """
    Represents a linked list of words and their counts.
    """
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def head(self):
        return self._head

    def update_count(self, word):
        """
        Updates the count of a word in the linked list,
        or adds a new node if the word is not present.

        Args:
            word (str): The word to update or add.
        """
        current = self._head
        # using while loop for till the current value is not none
        while current is not None:
            if current.word() == word:
                current.incr()
                return
            current = current.next()
        new_node = Node(word)
        new_node.set_next(self._head)
        self._head = new_node

    def rm_from_hd(self):
        """
        Removes the first node from the linked list.

        Returns:
            Node: The removed node.

        Raises:
            IndexError: If the list is empty.
        """
        removed_node = self._head
        self._head = self._head.next()
        return removed_node

    def insert_after(self, node1, node2):
        """
        Inserts node2 after node1 in the linked list.

        Args:
            node1 (Node): The node to insert after.
            node2 (Node): The node to insert.
        """
        if node1 is None:
            node2.set_next(self._head)
            self._head = node2
        else:
            node2.set_next(node1.next())
            node1.set_next(node2)

    def sort(self):
        """
        This method sorts the linked list in descending
        order based on the count of each word.
        It uses the insertion sort algorithm
        to rearrange the nodes in the list.
        """
        if self._head is None or self._head.next() is None:
            return
        sorted_head = None
        current = self._head
        # using while loop for till the current value is not none
        while current is not None:
            next_node = current.next()
            current.set_next(None)
            # Insert the current node into the sorted list
            if sorted_head is None or current.count() > sorted_head.count():
                current.set_next(sorted_head)
                sorted_head = current
            else:
                temp = sorted_head
                # using while loop for till the current value is not none
                while   temp.next() is not None and \
                        temp.next().count() > current.count():
                    temp = temp.next()
                # Insert after temp
                current.set_next(temp.next())
                temp.set_next(current)
            current = next_node
        self._head = sorted_head

    def get_nth_highest_count(self, n):
        """
        Returns the count of the nth node in the linked list.

        Args:
            n (int): The position of the node.

        Returns:
            int: The count of the nth node.
        """
        current = self._head
        count = 0
        while current is not None:
            if count == n:
                return current.count()
            current = current.next()
            count += 1
        return 0

    def print_upto_count(self, n):
        """
        Prints all words with count greater than or equal to n.

        Args:
            n (int): The minimum count to print.
        """
        current = self._head

        while current is not None and current.count() >= n:
            print(f"{current.word()} : {current.count()}")
            current = current.next()

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string representation of the linked list.
        """
        result = ""
        current = self._head
        while current is not None:
            result += str(current)
            if current.next() is not None:
                result += "\n"
            current = current.next()

        return result
def clean_title(title):
    """
    Cleans a title by removing punctuation and short words.

    Args:
        title (str): The title to clean.

    Returns:
        list: A list of cleaned words.
    """
    i = 0
    while i < len(string.punctuation):
        char = string.punctuation[i]
        title = title.replace(char, " ")
        i += 1
    # Convert to lowercase and split into words
    words = title.lower().split()
    cleaned_words = []
    i = 0
    while i < len(words):
        word = words[i]
        if len(word) > 2:
            cleaned_words.append(word)
        i += 1
    return cleaned_words

def main():
    input_file = input()
    word_counts = LinkedList()
    f = open(input_file, 'r')
    reader = csv.reader(f)
    row = next(reader, None)
    # Use a while loop to process each row in the CSV file
    while row is not None:
        if not row or row[0].startswith('#'):
            row = next(reader, None)
            # Move to the next row
            continue
        title = row[4]
        cleaned_words = clean_title(title)
        for word in cleaned_words:
            word_counts.update_count(word)
        row = next(reader, None)
    f.close()
    word_counts.sort()
    n = int(input())
    k = word_counts.get_nth_highest_count(n)
    word_counts.print_upto_count(k)
main()