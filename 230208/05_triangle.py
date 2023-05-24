def solution(sides):

    maxidx = sides.index(max(sides))
    maxVal = max(sides)
    sides.remove(maxVal)
    return (1 if maxVal < sum(sides) else 2)


    # if maxVal < sum(sides):
    #     print(1)
    # else:
    #     print(2)
    

    
    


solution([199,72,222])
solution([3,6,2])
solution([1,2,3])