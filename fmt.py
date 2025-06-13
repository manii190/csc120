def fmt(spec, values):
    if "{}" not in spec:
        return spec
    before, _, after = spec.partition("{}")
    return before + str(values[0]) + fmt(after, values[1:])
