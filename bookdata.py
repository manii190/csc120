# Lab 4 Problem 1- exercise on using a class

class BookData:
    def __init__(self, author, title, rating):
        self._author = author
        self._title = title
        self._rating = rating

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_rating(self):
        return self._rating

    def __str__(self):
        return self._title + " - " + self._author + " - " + str(self._rating)

def process_data(filename):
    f =open(filename,"r")
    for lines in f:
        words=lines.strip().split()
    dict ={}
    dict(words[0])=BookData(words[0],words[1],int(words[2]))
    return dict

def main():
    filename= input("Enter filename: ")
    dict=process_data(filename)
    for book in dict:
        print(dict[book].__str__())
    prompt = ''
    while prompt != 'done':
        title = input("Book title: ")
        if  title in dict:
            print(f"Rating is {dict{title}.get_rating()}")
        if title not in dict:
            print("There is no information on that book")
        prompt = input('Enter "done" if finished: ')
 
main()
'''def main():
    values="William Faulkner: The Sound and the Fury"
    index=values.find(":")
    author=line[:index]
    title=line[index+1:]
main()
'''