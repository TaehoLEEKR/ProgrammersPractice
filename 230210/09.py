def solution(numbers):
    numbers.sort()
    print(max(numbers[0]*numbers[1] , numbers[-1]* numbers[-2]))



solution([1, 2, -3, 4, -5,-6])