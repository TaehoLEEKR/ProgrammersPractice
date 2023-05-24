from collections import deque

def solution(A,B):
    A, B = deque(A), deque(B)
    
    for cnt in range(len(A)):
        if A == B:
            return cnt
        
        A.rotate()
    
    return -1



solution("apple","elppa")
solution("hello","ohell")