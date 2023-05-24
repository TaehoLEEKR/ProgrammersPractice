def solution(my_string):
    lst = list(my_string)
    res = []
    for i in lst:
        if i.isupper():
            res.append(i.lower())
        elif i.islower():
            res.append(i.upper())
    return "".join(map(str,res))


solution("cccCCC")