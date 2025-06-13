def palindrome_list(arglist):
    if len(arglist) <= 1:
        return True
    if arglist[0] != arglist[-1]:
        return False
    return palindrome_list(arglist[1:-1])
