def solution(n):
    if n % 2 == 0:
        #짝수일 때
        return sum(i ** 2 for i in range(2, n+1, 2))
    else:
        #홀수일 때
        return sum(range(1, n+1, 2))