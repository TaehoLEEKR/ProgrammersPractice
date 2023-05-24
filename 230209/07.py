from collections import Counter


def solution(s):
    count = Counter(s)
    lst = []
    for i,k in count.items():
        if k == 1:
            lst.append(i)
    return "".join(map(str,lst))
        


solution("abcabcadc")