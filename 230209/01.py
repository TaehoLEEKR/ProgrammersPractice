def solution(array, n):
    lst = []
    array.sort()
    for i in array:
        lst.append(abs(i-n))
    print(array[lst.index(min(lst))])

solution([10,11,12],13)