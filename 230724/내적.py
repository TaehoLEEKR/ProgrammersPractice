def solution(a, b):
    sums = 0
    for i,k in zip(a,b):
        sums += (i*k)
    return sums
    #