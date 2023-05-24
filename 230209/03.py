def solution(cipher, code):
    lst = []

    for i,k in enumerate(cipher,1):
        print(i,k)
        if( i % code == 0):
            lst.append(k)

    return "".join(map(str,lst))

solution("dfjardstddetckdaccccdegk",4)