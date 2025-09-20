def solution(num, n):
    result = divmod(num, n)[1]
    return 1 if result == 0 else 0