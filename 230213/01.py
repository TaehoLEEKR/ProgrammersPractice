from collections import Counter
def solution(before, after):
    
    beforeCnt = Counter(before)
    aftereCnt = Counter(after)
    if beforeCnt == aftereCnt:
        return 1
    else:
        return 0

solution("olleh","hello")