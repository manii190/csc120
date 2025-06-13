"""Implement your class here"""
class Word:
    def __init__(self, word):
        self._word = word

    def __str__(self):
        return self._word.lower()
    def __eq__(self,other):
        return sorted(self._word.lower())==sorted(other._word.lower())

    pass






"""DO NOT MODIFY ANYTHING BELOW THIS LINE"""

def test01():
    word1 = Word("post")
    word2 = Word("stop")
    return word1 == word2

def test02():
    word1 = Word("")
    word2 = Word("")
    return word1 == word2

def test03():
    w1 = Word("aBLE")
    return str(w1)

def test04():
    w1 = Word("Able")
    w2 = Word("Baker")
    return w1 == w2

def test05():
    w1 = Word("Hi there!")
    w2 = Word("Hit here!")
    return w1 == w2

def test06():
    w1 = "string**"
    w2 = "string@@"
    return w1 == w2
    
def test07():
    w1 = Word("indicatory")
    w2 = Word("dictionary")
    return w1 == w2
    
def anagrams(test_num):
    test_func = globals()['test{0}'.format(test_num)]
    return test_func()