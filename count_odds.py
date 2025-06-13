def count_odds(arglist):
    if not arglist:
        return 0
    if arglist[0] % 2 != 0:
        return 1 + count_odds(arglist[1:])
    return count_odds(arglist[1:])