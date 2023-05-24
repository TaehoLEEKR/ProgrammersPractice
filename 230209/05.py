def solution(numbers):
    lst = ["zero", "one" ,"two" ,"three" ,"four","five", "six","seven" ,"eight","nine" ]
    
    for i,k in enumerate(lst):
        numbers = numbers.replace(k,str(i))
    return numbers


solution("onetwothreefourfivesixseveneightnine")