def count_occurrences(alist,value):
    if  not  alist:
        return 0
    if alist[0] != value:
        return count_occurrences(alist[1:],value)
    if alist[0] == value:
        return 1+ count_occurrences(alist[1:],value)
print(count_occurrences([2,8,2,6,2,9],2))