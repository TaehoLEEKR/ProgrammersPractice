def solution(n):
    sorting = sorted([int(i) for i in str(n)],reverse=True)
    return int("".join(map(str,sorting)))