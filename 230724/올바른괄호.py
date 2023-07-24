def solution(s):
    lst =[i for i in s]
    res = []

    try:
        for i in lst:
            if i == "(":
                res.append(i)
            else:
                res.pop()
        if len(res) == 0:
            return True
        else:
            return False
    except:
        return False
#