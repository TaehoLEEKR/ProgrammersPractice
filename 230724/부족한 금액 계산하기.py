import sys
def dfs(price , money ,count):
    sys.setrecursionlimit(5000)
        if money < 0:
            return abs(money)
        else:
            return 0
    return dfs(price, money - price*count, count - 1)
        
def solution(price, money, count):
    return dfs(price,money,count)
#