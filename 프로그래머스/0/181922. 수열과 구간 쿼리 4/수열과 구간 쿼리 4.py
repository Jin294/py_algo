def solution(arr, queries):
    answer = arr[:]
    for s, e, k in queries:
        for idx in range(s, e+1):
            if idx % k == 0:
                answer[idx] += 1
    return answer