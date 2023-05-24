def solution(id_pw, db):
    if id_pw in db:
        return "login"
    elif id_pw not in db and id_pw[0] in db:
        return "fail"
    elif id_pw not in db:
        return "wrong pw"
    
    



solution(["meosseugi", "1234"],[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]] )