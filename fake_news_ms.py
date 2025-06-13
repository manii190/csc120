"""
venna mani abhiram reddy 
cs-120
project-fake_new_ms
This code process a CSV file, 
extract and count words from the "title" field,
sort those words based on their frequency of occurrence, 
and then display the most frequent words.


"""

import sys
import csv
import string

class Word:
    def __init__(self, word):
        self._word = word
        self._count = 1

    def word(self):
        return self._word

    def count(self):
        return self._count

    def incr(self):
        self._count += 1

    def __lt__(self, other):
        return self._word < other.word()

    def __str__(self):
        return f"{self._word} : {self._count}"

    def __repr__(self):
        return f"Word('{self._word}', {self._count})"

def msort(L):
    """
    Perform a recursive merge sort on a list of Word objects.
    
    Parameters:
    L (list): A list of Word objects to be sorted.
    
    Returns:
    list: A sorted list of Word objects.
    """
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = msort(L[:mid])
    right = msort(L[mid:])
    return merge(left, right)

def merge(left, right):
    """
    Merge two sorted lists of Word objects into a single sorted list.
    
    Parameters:
    left (list): The left sorted list.
    right (list): The right sorted list.
    
    Returns:
    list: A merged and sorted list of Word objects.
    """
    result = []
    i = 0
    j = 0
    # # While loop to compare elements from left and right lists
    while i < len(left) and j < len(right):
        left_word = left[i]
        right_word = right[j]
        if left_word.count() > right_word.count():
            result.append(left_word)
            i += 1
        elif left_word.count() < right_word.count():
            result.append(right_word)
            j += 1
        else: 
            if left_word.word() < right_word.word():
                result.append(left_word)
                i += 1
            else:
                result.append(right_word)
                j += 1
    #  While loop to append any remaining words from the left list
    while i < len(left):
        result.append(left[i])
        i += 1
    #  While loop to append any remaining words from the right list
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
def main():
    sys.setrecursionlimit(4000)
    filename = input(" ")
    words = []
    file = open(filename, 'r')
    reader = csv.reader(file)
    # # While loop to process each row in the CSV file
    while True:
        row = next(reader, None)
        if row is None:
            break
        if row and row[0].startswith('#'):
            continue
        if len(row) > 4:
            title = row[4].lower()
            punctuation = string.punctuation
            spaces = ' ' * len(punctuation)
            translation_table = str.maketrans(punctuation, spaces)
            title = title.translate(translation_table)
            word_list = title.split()
            i = 0
            # # While loop to process each word in the word list
            while i < len(word_list):
                word = word_list[i]
                if len(word) > 2:
                    found = False
                    index = 0
                    # While loop to check if word already exists in words list
                    while index < len(words):
                        if words[index].word() == word:
                            words[index].incr()
                            found = True
                            break
                        index += 1
                    if not found:
                        words.append(Word(word))
                i += 1
    sorted_words = msort(words)
    n = int(input(" "))
    if len(sorted_words) > n:
        k = sorted_words[n].count()
        print("File: N:", end=" ")
        # While loop to print sorted words with count >= k
        i = 0
        while i < len(sorted_words):
            word = sorted_words[i]
            if word.count() >= k:
                print(word)
            i += 1
    file.close()
main()
