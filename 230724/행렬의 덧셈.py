def solution(arr1, arr2):
    answer = []

    for i, k in zip(arr1, arr2):
        temp = []
        
        for x, y in zip(i, k):
            
            temp.append(x + y)
            
        answer.append(temp)

    return answer