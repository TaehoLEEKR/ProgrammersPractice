import math
def solution(n):
    lst = []
    for i in range(1,math.sqrt(n)):
        if(n % i ==0):
            lst.append(i)
            if(n / i != i):
                lst.append(int(n/i))
    lst.sort()
    return lst



solution(24)