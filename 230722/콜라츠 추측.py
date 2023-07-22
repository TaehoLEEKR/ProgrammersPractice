def dfs(num,cnt):
    if cnt > 500 : return -1
    if num == 1:
        return cnt
    else:
        cnt += 1
        if num % 2 == 0:
            num = num // 2 
        else:
            num = (num * 3) + 1
    return dfs(num, cnt)

def solution(num):
    answer = 0
    return dfs(num,answer)