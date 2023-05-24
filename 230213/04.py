def solution(dots):

    
    x= max(dots)[0] - min(dots)[0]
    y= max(dots)[1] - min(dots)[1]
    
    return x*y
    
    




solution([[1, 1], [2, 1], [2, 2], [1, 2]])
solution([[-1, -1], [1, 1], [1, -1], [-1, 1]])