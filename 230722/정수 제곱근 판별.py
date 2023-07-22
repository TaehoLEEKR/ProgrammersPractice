import math

def solution(n):
    if round(math.sqrt(n))**2 == n:
        return ((round(math.sqrt(n))+1)**2)
    else:
        return -1
        