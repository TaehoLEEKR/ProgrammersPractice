def solution(n):
    start,end,sums,count = 1,1,0,0

    while start <= n:
        if sums < n:
            sums += end
            end += 1
        elif sums > n:
            sums -= start
            start += 1
        else:
            count += 1
            sums -= start
            start += 1

    return count
