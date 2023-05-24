from itertools import combinations
import math
def fac(n):
    if(n == 1):
        return n
    return n * fac(n-1)

def solution(balls, share):
    #return len(list(combinations([i for i in range(balls)],share)))
    res = fac(balls) // (fac(balls-share) * fac(share))
    return print(res)


def solution1(balls, share):
    return math.comb(balls,share)
solution(6,4)
solution1(5,3)

print(fac(5))