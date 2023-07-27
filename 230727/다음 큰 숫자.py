def solution(n):
    binary_n = bin(n)[2:]
    i = 1
    while True:
        next_big = bin(n+i)[2:]
        if binary_n.count("1") == next_big.count("1") and  n < int(next_big) :
            return int(next_big,2)
        else:
            i +=1
            
        