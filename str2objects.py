def str2objects(spec):
    if len(spec) == 0:
        return []
    parts = spec.split(None, 1)
    first = parts[0]
    if first == "dict":
        obj = {}
    elif first == "list":
        obj = []
    else:  # first == "str"
        obj = ""
    if len(parts) > 1:
        return [obj] + str2objects(parts[1])
    return [obj]