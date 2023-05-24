def solution(array):
    return list(map(int,list(str(int("".join(map(str,array))))))).count(7)
    
#list(map(int, list(str(c))))

solution([7,77,17,707,717])