def solution(left, right):
    answer = 0
    arr = []
    for i in range(left,right+1):
        answer = 0
        for k in range(1,i+1):
            if i % k == 0:
                answer +=1
        if answer % 2 == 0:
            arr.append(i)
        else:
            arr.append(-i)
    return sum(arr)
    #