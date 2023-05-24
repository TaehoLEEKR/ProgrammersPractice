def solution(s):
    lst = list(s.split(" "))
    res = 0
    chk = 0
    for i in lst:
        if i != 'Z':
            res += int(i)
            chk = int(i)
        elif i == 'Z':
            res -= chk
    return res
solution("1 2 Z 3")