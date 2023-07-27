def solution(s):
    answer = s.split(" ")
    lst = []
    for i in answer:
        for k in range(0,len(i)):
            if k % 2 == 0:
                lst.append(i[k].upper())
            else:
                lst.append(i[k].lower())
        lst.append(" ")
    lst.pop()
    return "".join(lst)