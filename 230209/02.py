def solution(order):
    lst = [int(i) for i in list(str(order)) if int(i) % 3 == 0 and int(i) != 0]
    
    return len(lst)


solution(0)