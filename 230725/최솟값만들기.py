def solution(A, B):
    A.sort() 
    B.sort()  
    min_sum = sum(a * b for a, b in zip(A, reversed(B))) 
    return min_sum

