def solution(number, n, m):
    result1 = number % n
    result2 = number % m
    return 1 if result1 == result2 == 0 else 0