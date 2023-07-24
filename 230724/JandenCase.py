def solution(s):
    strs  = s.split(" ")
    print(strs)
    for i in range(len(strs)):
        strs[i] = strs[i].capitalize()
    return " ".join(strs)
            