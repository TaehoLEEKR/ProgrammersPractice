def solution(dot):
    x,y = dot
    point = [
        (3,2),
        (4,1)
        ]
    return (point[x > 0][y > 0])


solution([-7,9])