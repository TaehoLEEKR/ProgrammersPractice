from collections import deque
def solution(numbers, direction):
    deq = deque(numbers)
    if direction == "right" :
        rightIdx = deq.pop()
        deq.appendleft(rightIdx)
    else:
        leftIdx = deq.popleft()
        deq.append(leftIdx)
    
    return list(deq)

solution([4,455,6,4,-1,45,6],"left")
solution([1,2,3],"right")