def reverse_string(s):
    st =""
    if len(s) == 0 :
        return ""
    return  s[-1]+ reverse_string(s[:-1])

print(reverse_string("mani"))