def solution(numbers):
    answer = set(range(10)) - set(numbers)
    return sum(answer)