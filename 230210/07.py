import math 
def solution(n):
    strs = str(math.sqrt(n))
    lst = strs.split(".")
    if lst[1] != '0':
        return 2
    else:
        return 1


solution(144)