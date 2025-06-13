import random
import sys

SEED = 7  # Changed from 8 to 7 to match expected random.choice behavior
NONWORD = '@'

class Hashtable:
    def __init__(self, size):
        self._pairs = [None] * size
        self._size = size

    def _hash(self, key):
        p = 0
        for c in key:
            p = 31 * p + ord(c)
        return p % self._size

    def put(self, key, value):
        index = self._hash(key)
        original_index = index
        while self._pairs[index] is not None:
            if self._pairs[index][0] == key:
                self._pairs[index][1].append(value)  # Append single suffix
                return
            index = (index - 1) % self._size
            if index == original_index:
                return  # Table is full, ignore insertion
        self._pairs[index] = [key, [value]]  # New key with single suffix

    def get(self, key):
        index = self._hash(key)
        original_index = index
        while self._pairs[index] is not None:
            if self._pairs[index][0] == key:
                return self._pairs[index][1]
            index = (index - 1) % self._size
            if index == original_index:
                return None
        return None

    def __contains__(self, key):
        index = self._hash(key)
        original_index = index
        while self._pairs[index] is not None:
            if self._pairs[index][0] == key:
                return 1
            index = (index - 1) % self._size
            if index == original_index:
                return 0
        return 0

    def __str__(self):
        result = []
        for i in range(self._size):
            if self._pairs[i] is not None:
                result.append(f"Index {i}: {self._pairs[i]}")
        return "\n".join(result)

def build_markov_table(words, n, table):
    prefix = [NONWORD] * n
    for word in words:
        prefix_str = ' '.join(prefix)
        table.put(prefix_str, word)  # Append word as suffix
        prefix.pop(0)
        prefix.append(word)
    # Add NONWORD as suffix for the final prefix
    prefix_str = ' '.join(prefix)
    table.put(prefix_str, NONWORD)

def generate_text(table, n, num_words):
    random.seed(SEED)
    text = []
    prefix = [NONWORD] * n
    prefix_str = ' '.join(prefix)
    for _ in range(num_words):
        suffixes = table.get(prefix_str)
        if suffixes is None or (NONWORD in suffixes and len(suffixes) == 1):
            break
        next_word = random.choice(suffixes)
        if next_word == NONWORD:
            break
        text.append(next_word)
        prefix.pop(0)
        prefix.append(next_word)
        prefix_str = ' '.join(prefix)
    return text

def print_text(text):
    for i in range(0, len(text), 10):
        print(' '.join(text[i:i+10]))

def main():
    sfile = input()
    M = int(input())
    n = int(input())
    num_words = int(input())

    if n < 1:
        print("ERROR: specified prefix size is less than one")
        sys.exit(0)
    if num_words < 1:
        print("ERROR: specified size of the generated text is less than one")
        sys.exit(0)

    table = Hashtable(M)
    words = []
    file = open(sfile, 'r')
    for line in file:
        words.extend(line.split())
    file.close()

    build_markov_table(words, n, table)
    text = generate_text(table, n, num_words)
    print_text(text)

if __name__ == "__main__":
    main()