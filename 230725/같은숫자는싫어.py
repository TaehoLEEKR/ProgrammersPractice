def solution(arr):
    stack = []
    for i in arr:
        if not stack or stack[-1] != i:
            stack.append(i)
        return stack