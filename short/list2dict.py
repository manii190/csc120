def list2dict(lis2d):
    new_dict={}
    for list in lis2d:
        new_dict[list[0]]=list[1:]
    return new_dict