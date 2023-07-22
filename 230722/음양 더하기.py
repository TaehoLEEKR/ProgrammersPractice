def solution(absolutes, signs):
    lst = list(zip(absolutes, signs))
    result = []
    for i,k in lst:
        if k ==  False:
            result.append(i*-1)
        else:
            result.append(i)
    return sum(result)