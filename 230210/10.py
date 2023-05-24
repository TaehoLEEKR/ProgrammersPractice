def solution(my_string):
    lst = [i.lower() for i in list(my_string)].sort()
    lst.sort()
    return "".join(map(str,lst))
    



solution("heLLo")