def solution(n, numlist):
    return [i for i in numlist if i % n == 0]
    


solution(3,[4, 5, 6, 7, 8, 9, 10, 11, 12])