def solution(quiz):
    lst = []
    for i in quiz:
        lst.append(i.split("="))
    res = []
    for i in lst:
        
        if int(i[1].lstrip()) != eval(i[0]):
            res.append("X")
        else:
            res.append("O")
    return res

    
        
        
    


solution(["3 - 4 = -3", "5 + 6 = 11"])
solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"])