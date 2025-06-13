def ngram(arglist, startpos, length):
    if startpos < 0:
        startpos += len(arglist)
    if startpos < 0 or startpos + length > len(arglist):
        return []
    else:
        return arglist[startpos:startpos + length]
print(ngram([11, 22, 33, 44, 55], 0, 3))