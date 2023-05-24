
def solution(num, k):
    try:
        lst = list(map(int, list(str(num))))
        return lst.index(k)+1
    except:
        return -1


solution(232443,4)