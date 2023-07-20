
answer = 0
def dfs(idx,sum,numbers,targer):
    global answer
    if idx == len(numbers) and targer == sum:
        answer +=1
        return
    if idx == len(numbers):
        return

    dfs(idx+1,sum+numbers[idx],numbers,targer)
    dfs(idx+1,sum-numbers[idx],numbers,targer)

def solution(numbers, target): 
    global answer
    dfs(0,0,numbers,target)
    return answer


print(solution([1, 1, 1, 1, 1],3))