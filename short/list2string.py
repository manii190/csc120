def list2string(arglist):
    if not arglist:
        return ''
    return arglist[0] + list2string(arglist[1:])
