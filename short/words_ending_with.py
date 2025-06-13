def words_ending_with(wordlist, tail):
    if len(tail)>0:
        new_list=[]
        for word in wordlist:
            if  word[-len(tail):]==tail:
                new_list.append(word)
        return  new_list
    else:
        return  wordlist