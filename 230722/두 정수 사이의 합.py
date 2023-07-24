def solution(a, b):
    
    if a > b: 
        a , b = b, a
    answer = ((b - a +1) / 2) * (a + b)
    return answer