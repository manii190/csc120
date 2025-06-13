def words_beginning_with(wordlist, head):
    if len(head)>0:
        new_list=[]
        for word in wordlist:
            if  word[0:len(head)]==head:
                new_list.append(word)
        return  new_list
    else:
        return  wordlist