
def gcd(n,m):
    while m > 0:
        tmp = n
        n = m
        m = tmp % m
    return n
def lcm(x,y,gcd):
    return x*y//gcd

def solution(n, m):
    answer = [gcd(n,m),lcm(n,m,gcd(n,m))]
    return answer
    #