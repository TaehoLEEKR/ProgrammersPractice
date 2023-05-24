def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)
def solution(n):
    lst = [fac(i) for i in range(1,11)]
    for i in range(0,len(lst)-1):
            if n >= lst[i] and n <= lst[i+1]:
                print(i+2)


solution(3628800)