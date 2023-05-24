def solution(my_string, num1, num2):
    lst = list(my_string)
    tmp = lst[num1]
    lst[num1],lst[num2] = lst[num2],tmp
    return "".join(map(str,lst))
    


solution("hello",1,2)