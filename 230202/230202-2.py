def solution(numbers):
    maxIdx = max(numbers)
    numbers.remove(maxIdx)
    maxIdx2 = max(numbers)
    return maxIdx*maxIdx2


solution([1,2,3,4,5])
solution([0,31,24,10,1,9])
