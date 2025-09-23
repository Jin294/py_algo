def solution(arr, queries):
    answer = arr[:]
    for idx1, idx2 in queries:
        num1 = answer[idx1]
        num2 = answer[idx2]
        
        answer[idx1] = num2
        answer[idx2] = num1
    return answer