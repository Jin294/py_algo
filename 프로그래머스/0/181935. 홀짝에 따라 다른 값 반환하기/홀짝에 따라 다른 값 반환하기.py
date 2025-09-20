def solution(n):
    answer = 0
    if n % 2 == 0:
        #짝수일 때
        while n > 0:
            answer += n**2
            n -= 2
    else:
        #홀수일 때
        while n > 0:
            answer += n
            n -= 2
    return answer