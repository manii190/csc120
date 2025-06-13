def shift_tuple(tup, value):
    if not tup:
        return (value,)
    return tup[1:] + (value,)