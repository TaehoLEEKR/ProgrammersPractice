def solution(n):
    primes = [2, 3, 5]  # 소인수로 사용할 소수들
    cnt = 0
    num = 1
    while cnt < n:
        cur = num
        for prime in primes:
            while cur % prime == 0:
                cur //= prime
        if cur == 1:
            cnt += 1
        num += 1
    return num - 1

print(solution(10))