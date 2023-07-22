def solution(arr):
    arr.pop(arr.index(min(arr)))
    return arr or [-1]