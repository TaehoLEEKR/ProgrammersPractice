binary_cnt = 0

def dfs(s, cnt):
    global binary_cnt

    if s == "1":
        return [cnt, binary_cnt]

    cnt += 1
    binary_cnt += s.count("0") 
    s = bin(s.count("1"))[2:]  

    return dfs(s, cnt)

def solution(s):
    return dfs(s, 0)

