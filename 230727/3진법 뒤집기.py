def decimal_to_ternary(n):
    ternary = ""
    while n > 0:
        n, remainder = divmod(n, 3)
        ternary = str(remainder) + ternary
    return ternary

def solution(n):
    ternary = decimal_to_ternary(n)
    print(ternary)
    decimal_result = 0
    power = 0
    for digit in ternary:
        decimal_result += int(digit) * (3 ** power)
        power += 1
    return decimal_result
