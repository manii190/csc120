import sys
import csv
import string

class Word:
    def _init_(self, word):
        self._word = word
        self._count = 1

    def word(self):
        return self._word

    def count(self):
        return self._count

    def incr(self):
        self._count += 1

    def _lt_(self, other):
        return self._word < other.word()

    def _str_(self):
        return f"{self._word} : {self._count}"

    def _repr_(self):
        return f"Word('{self._word}', {self._count})"

def msort(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = msort(L[:mid])
    right = msort(L[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].count() > right[j].count() or \
           (left[i].count() == right[j].count() and \
            left[i].word() < right[j].word()):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def main():
    sys.setrecursionlimit(4000)
    filename = input()
    words = []

    file = open(filename, 'r') 
    reader = csv.reader(file)
    for row in reader:
        if row and row[0].startswith('#'):
            continue
        if len(row) > 4:
            title = row[4].lower()
            title = title.translate(str.maketrans(\
                string.punctuation, ' ' * len(string.punctuation)))
            word_list = title.split()
            for word in word_list:
                if len(word) > 2:
                    found = False
                    for w in words:
                        if w.word() == word:
                            w.incr()
                            found = True
                            break
                    if not found:
                        words.append(Word(word))

    sorted_words = msort(words)

    n = int(input())
    if sorted_words and len(sorted_words) > n:
        k = sorted_words[n].count()
        print("File: N: ", end = "")
        for word in sorted_words:
            if word.count() >= k:
                print(word)
    file.close()
main()