def solution(rsp):
    win = {
        "2" : "0",
        "0" : "5",
        "5" : "2",
    }
    return "".join(map(str, [win[i] for i in list(rsp)]))

solution("205")