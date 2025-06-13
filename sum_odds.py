def sum_odds(arglist):
    if not arglist:
        return 0
    if arglist[0] % 2 != 0:
        return arglist[0] + sum_odds(arglist[1:])
    return sum_odds(arglist[1:])