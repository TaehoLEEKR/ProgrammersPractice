
def solution(n):
    s = set()
    for i in range(2, int(n ** .5) + 1):
        while n % i == 0:
            n //= i
            s.add(i)
    if n > 1:
        s.add(n)
    return sorted(s)