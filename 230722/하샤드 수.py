def solution(x):
    
    lst = [int(i) for i in str(x)]
    return True if x % sum(lst) == 0 else False