def solution(s):
    lst = [int(i) for i in s.split(" ")]
    return f'{min(lst)} {max(lst)}'
    #