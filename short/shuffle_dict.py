def shuffle_dict(somedict):
    sorted_keys=[]
    sorted_values=[]
    dictorny={}
    for keys,values in somedict.items():
        sorted_keys.append(keys)
        sorted_values.append(values)
    sorted_keys=sorted(sorted_keys)
    sorted_values=sorted(sorted_values)
    for i in range(len(sorted_keys)):
        dictorny[sorted_keys[i]]=sorted_values[i]
    return  dictorny