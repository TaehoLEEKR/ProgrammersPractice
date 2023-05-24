def solution(my_string):
    my_string = list(my_string)
    my_string.sort()
    lst = []
    for i in my_string:
        if ord(i) >= 48 and ord(i) <=57:
            lst.append(int(i))
    return sum(lst)


solution("p2o4i8gj2")