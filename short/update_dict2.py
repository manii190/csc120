def update_dict2(dict2, keys1, keys2, value):
    newdict2 = {}
    for keys, values in dict2.items():
        newdict2[keys] = values
    if keys1 not in newdict2:
        newdict2[keys1] = {}
    inner_dict = {}
    if keys1 in newdict2:
        for k, v in newdict2[keys1].items():
            inner_dict[k] = v
    inner_dict[keys2] = value
    newdict2[keys1] = inner_dict
    return newdict2